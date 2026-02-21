# -*- coding: utf-8 -*-
import json
import sys
sys.path.append('..')
from base.spider import Spider
import requests

class Spider(Spider):
    def init(self, extend=""):
        self.host = 'https://ev5356.970xw.com'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; V2196A Build/PQ3A.190705.08211809; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/145.0.7626.0 Mobile Safari/537.36;webank/h5face;webank/1.0;netType:NETWORK_WIFI;appVersion:416;packageName:com.jp3.xg3',
            'Referer': self.host
        }
        self.ihost = self._get_img_domain()
        self.filter_config = self._load_filter(extend)

    def _get_img_domain(self):
        """获取图片域名（与原 Java 逻辑一致）"""
        try:
            data = requests.get(f"{self.host}/api/appAuthConfig", headers=self.headers).json()
            host = data['data']['imgDomain']
            return f"https://{host}" if not host.startswith('http') else host
        except:
            return self.host  # 降级使用主域名

    def _load_filter(self, extend):
        """加载筛选配置：extend 可以是 URL 或 JSON 字符串"""
        if not extend:
            return {}
        if extend.startswith('http'):
            try:
                resp = requests.get(extend, headers=self.headers, timeout=5)
                return resp.json()
            except:
                return {}
        try:
            return json.loads(extend)
        except:
            return {}

    def getName(self):
        return "JianPian"

    def homeContent(self, filter):
        classes = [
            {'type_id': '1', 'type_name': '电影'},
            {'type_id': '2', 'type_name': '电视剧'},
            {'type_id': '3', 'type_name': '动漫'},
            {'type_id': '4', 'type_name': '综艺'}
        ]
        # 如果配置中有筛选器则使用，否则返回空筛选器（与原 Java 一致）
        filters = self.filter_config if self.filter_config else {}
        return {
            'class': classes,
            'filters': filters
        }

    def homeVideoContent(self):
        url = f"{self.host}/api/slide/list?pos_id=88"
        data = requests.get(url, headers=self.headers).json()
        videos = [{
            'vod_id': item['jump_id'],
            'vod_name': item['title'],
            'vod_pic': f"{self.ihost}{item['thumbnail']}",
            'vod_remarks': "",
            'style': json.dumps({"type": "rect", "ratio": 1.33})
        } for item in data['data']]
        return {'list': videos}

    def categoryContent(self, tid, pg, filter, extend):
        # 处理以 "/{pg}" 结尾的 tid（搜索分页）
        if tid.endswith('/{pg}'):
            key = tid.split('/')[0]
            return self.searchContent(key, False, pg)

        # 特殊分类：50, 99, 111 使用 dyTag 接口（与原 Java 一致）
        if tid in ['50', '99', '111']:
            url = f"{self.host}/api/dyTag/list?category_id={tid}&page={pg}"
            data = requests.get(url, headers=self.headers).json()
            videos = []
            for item in data['data']:
                for sub in item.get('dataList', []):
                    videos.append({
                        'vod_id': sub['id'],
                        'vod_name': sub['title'],
                        'vod_pic': f"{self.ihost}{sub.get('path', sub.get('thumbnail'))}",
                        'vod_remarks': sub.get('mask', ''),
                        'vod_year': sub.get('year', '')
                    })
            return {
                'list': videos,
                'page': pg,
                'pagecount': 99999,
                'limit': 20,
                'total': 99999
            }

        # 普通分类使用 crumb/list 接口（参数与原 Java 完全一致）
        params = {
            'fcate_pid': tid,
            'page': pg,
            'area': extend.get('area', '0'),
            'year': extend.get('year', '0'),
            'type': '0',
            'sort': extend.get('by', 'updata'),  # 默认排序与原 Java 相同
            'category_id': ''  # 保留空参数以匹配 Java 的 URL
        }
        url = f"{self.host}/api/crumb/list"
        data = requests.get(url, params=params, headers=self.headers).json()
        videos = [{
            'vod_id': item['id'],
            'vod_name': item['title'],
            'vod_pic': f"{self.ihost}{item['path']}",
            'vod_remarks': item.get('mask', ''),
            'vod_year': item.get('year', '')
        } for item in data['data']]
        return {
            'list': videos,
            'page': pg,
            'pagecount': 99999,
            'limit': 15,
            'total': 99999
        }

    def detailContent(self, ids):
        id = ids[0]
        url = f"{self.host}/api/video/detailv2?id={id}"
        data = requests.get(url, headers=self.headers).json()
        res = data['data']

        # 解析类型名称（与原 Java 一致）
        type_names = [t['name'] for t in res.get('types', [])]
        type_name = '/'.join(type_names)

        # 解析播放线路（生成与原 Java 完全相同的 vod_play_from 和 vod_play_url）
        play_from = []
        play_url = []
        source_list = res.get('source_list_source', [])
        for source in source_list:
            name = source.get('name', '未知线路')
            play_from.append(name)
            episodes = []
            for part in source.get('source_list', []):
                ep_name = part.get('source_name') or part.get('weight', '')
                ep_url = part.get('url', '')
                if ep_url:
                    episodes.append(f"{ep_name}${ep_url}")
            play_url.append('#'.join(episodes))

        # 如果没有线路，尝试兼容旧字段
        if not play_from:
            simple_play = res.get('play_url')
            if simple_play:
                play_from = ['常规线路']
                play_url = [simple_play]

        vod = {
            'vod_id': id,
            'vod_name': res.get('title', ''),
            'vod_pic': f"{self.ihost}{res.get('path', res.get('thumbnail', ''))}",
            'type_name': type_name,
            'vod_year': res.get('year', ''),
            'vod_area': res.get('area', ''),
            'vod_remarks': res.get('mask', ''),
            'vod_actor': res.get('actors', ''),
            'vod_director': res.get('directors', ''),
            'vod_content': res.get('description', ''),
            'vod_play_from': '$$$'.join(play_from),   # 与原 Java 完全一致
            'vod_play_url': '$$$'.join(play_url)      # 与原 Java 完全一致
        }
        return {'list': [vod]}

    def playerContent(self, flag, id, vipFlags):
        # 返回与原 Java 相同的 JSON 结构（包含 url 和 header）
        return {
            'url': id,
            'header': self.headers
        }

    def searchContent(self, key, quick, pg="1"):
        url = f"{self.host}/api/v2/search/videoV2"
        params = {'key': key, 'category_id': 88, 'page': pg, 'pageSize': 20}
        data = requests.get(url, params=params, headers=self.headers).json()
        videos = [{
            'vod_id': item['id'],
            'vod_name': item['title'],
            'vod_pic': f"{self.ihost}{item.get('thumbnail', '')}",
            'vod_remarks': item.get('mask', ''),
            'vod_year': item.get('year', '')
        } for item in data.get('data', [])]
        return {
            'list': videos,
            'limit': 20
        }

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass

    def destroy(self):
        pass

    def localProxy(self, param):
        pass

    def liveContent(self, url):
        pass