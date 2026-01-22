```python
# -*- coding: utf-8 -*-
# @Author  : Doubebly
# @Time    : 2025/3/23 21:55
import base64
import sys
import time
import json
import requests
sys.path.append('..')
from base.spider import Spider


class Spider(Spider):
    def getName(self):
        return "Litv"

    def init(self, extend):
        self.extend = extend
        try:
            self.extendDict = json.loads(extend)
        except:
            self.extendDict = {}

        proxy = self.extendDict.get('proxy', None)
        if proxy is not None:
            self.is_proxy = False
        else:
            self.proxy = proxy
            self.is_proxy = True
        pass

    def getDependence(self):
        return []

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass


    def liveContent(self, url):
        # 使用PHP代码中的所有频道数据，但保持Py代码的输出格式
        channels = [
            # 以下为PHP代码中的所有频道数据
            ("民視", "4gtv-4gtv002", 1, 11, "民視", "民視", "綜合頻道"),
            ("民視第一台", "4gtv-4gtv003", 1, 7, "民視第一台", "民視第一台", "綜合頻道"),
            ("民視新聞台", "litv-ftv13", 1, 7, "民視新聞台", "民視新聞台", "新聞財經"),
            ("民視台灣台", "4gtv-4gtv001", 1, 7, "民視台灣台", "民視台灣台", "綜合頻道"),
            ("民視影劇台", "litv-ftv09", 1, 6, "民視影劇台", "民視影劇台", "電影戲劇"),
            ("民視旅遊台", "litv-ftv07", 1, 6, "民視旅遊台", "民視旅遊台", "科教紀實"),
            ("民視綜藝台", "4gtv-4gtv004", 1, 9, "民視綜藝台", "民視綜藝台", "綜藝娛樂"),
            ("中视", "4gtv-4gtv040", 1, 7, "中视", "中視", "綜合頻道"),
            ("中视新闻", "4gtv-4gtv074", 1, 6, "中视新闻", "中視新聞台", "新聞財經"),
            ("中天新闻", "4gtv-4gtv009", 2, 9, "中天新闻", "中天新聞台", "新聞財經"),
            ("華視", "4gtv-4gtv041", 1, 7, "華視", "華視", "綜合頻道"),
            ("華視新聞", "4gtv-4gtv052", 1, 6, "華視新聞", "華視新聞", "新聞財經"),
            ("靖天綜合台", "4gtv-4gtv046", 1, 7, "靖天綜合台", "靖天綜合台", "綜合頻道"),
            ("靖天國際台", "4gtv-4gtv063", 1, 8, "靖天國際台", "靖天國際台", "綜合頻道"),
            ("靖天戲劇台", "4gtv-4gtv058", 1, 9, "靖天戲劇台", "靖天戲劇台", "電影戲劇"),
            ("靖天日本台", "4gtv-4gtv047", 1, 2, "靖天日本台", "靖天日本台", "綜合頻道"),
            ("靖天映畫台", "4gtv-4gtv055", 1, 9, "靖天映畫台", "靖天映畫台", "電影戲劇"),
            ("靖天卡通台", "4gtv-4gtv044", 1, 7, "靖天卡通台", "靖天卡通台", "卡通動漫"),
            ("靖天育樂台", "4gtv-4gtv062", 1, 9, "靖天育樂台", "靖天育樂台", "綜藝娛樂"),
            ("靖天資訊台", "4gtv-4gtv065", 1, 9, "靖天資訊台", "靖天資訊台", "新聞財經"),
            ("靖天電影台", "4gtv-4gtv061", 1, 7, "靖天電影台", "靖天電影台", "電影戲劇"),
            ("靖天歡樂台", "4gtv-4gtv054", 1, 9, "靖天歡樂台", "靖天歡樂台", "綜藝娛樂"),
            ("龍華偶像台", "litv-xinchuang12", 10003, 20000, "龍華偶像台", "龍華偶像台", "電影戲劇"),
            ("龍華卡通台", "litv-xinchuang01", 10002, 20000, "龍華卡通台", "龍華卡通台", "卡通動漫"),
            ("龍華戲劇台", "litv-xinchuang18", 10003, 20000, "龍華戲劇台", "龍華戲劇台", "電影戲劇"),
            ("龍華日韓台", "litv-xinchuang11", 10003, 20000, "龍華日韓台", "龍華日韓台", "電影戲劇"),
            ("龍華經典台", "litv-xinchuang21", 10003, 20000, "龍華經典台", "龍華經典台", "電影戲劇"),
            ("龍華電影台", "litv-xinchuang03", 10003, 20000, "龍華電影台", "龍華電影台", "電影戲劇"),
            ("龍華洋片台", "litv-xinchuang02", 10003, 20000, "龍華洋片台", "龍華洋片台", "電影戲劇"),
            ("靖洋戲劇台", "4gtv-4gtv045", 1, 7, "靖洋戲劇台", "靖洋戲劇台", "電影戲劇"),
            ("靖洋卡通-Nice-Bingo", "4gtv-4gtv057", 1, 7, "靖洋卡通-Nice-Bingo", "靖洋卡通NiceBingo", "卡通動漫"),
            ("寰宇新聞台", "litv-longturn14", 1, 6, "寰宇新聞台", "寰宇新聞台", "新聞財經"),
            ("寰宇新聞台灣台", "4gtv-4gtv156", 1, 8, "寰宇新聞台灣台", "寰宇新聞台灣台", "新聞財經"),
            ("寰宇財經台", "4gtv-4gtv158", 1, 2, "寰宇財經台", "寰宇財經台", "新聞財經"),
            ("TVBS欢乐", "4gtv-4gtv068", 1, 8, "TVBS欢乐", "TVBS歡樂台", "綜藝娛樂"),
            ("TVBS精采", "4gtv-4gtv067", 1, 9, "TVBS精采", "TVBS精采台", "綜藝娛樂"),
            ("八大精彩台", "4gtv-4gtv034", 1, 7, "八大精彩台", "八大精彩台", "綜藝娛樂"),
            ("八大綜藝台", "4gtv-4gtv039", 1, 6, "八大綜藝台", "八大綜藝台", "綜藝娛樂"),
            ("ELTA娛樂", "4gtv-4gtv070", 1, 9, "ELTA娛樂", "ELTA娛樂台", "綜藝娛樂"),
            ("ELTA生活英語", "litv-xinchuang20", 10003, 20000, "ELTA生活英語", "ELTV生活英語", "科教紀實"),
            ("东森新闻", "4gtv-4gtv152", 1, 7, "东森新闻", "東森新聞", "新聞財經"),
            ("东森财经", "4gtv-4gtv153", 1, 6, "东森财经", "東森財經新聞", "新聞財經"),
            ("鏡電視新聞台", "4gtv-4gtv075", 1, 6, "鏡電視新聞台", "鏡電視新聞台", "新聞財經"),
            ("亞洲旅遊台", "4gtv-4gtv076", 1, 7, "亞洲旅遊台", "亞洲旅遊台", "科教紀實"),
            ("GINX-Esports-TV", "4gtv-4gtv053", 1, 9, "GINX-Esports-TV", "GINXEsportsTV", "體育競技"),
            ("时尚运动X", "4gtv-4gtv014", 1, 6, "时尚运动X", "時尚運動X", "體育競技"),
            ("智林体育", "4gtv-4gtv101", 1, 6, "智林体育", "智林體育台", "體育競技"),
            ("TraceSports", "4gtv-4gtv077", 1, 5, "TraceSports", "TraceSports", "體育競技"),
            ("影迷數位電影台", "4gtv-4gtv011", 1, 7, "影迷數位電影台", "影迷數位電影台", "電影戲劇"),
            ("AMC-最愛電影", "4gtv-4gtv017", 1, 7, "AMC-最愛電影", "AMC電影台", "電影戲劇"),
            ("公視戲劇台", "4gtv-4gtv042", 1, 7, "公視戲劇台", "公視戲劇台", "電影戲劇"),
            ("采昌影劇台", "4gtv-4gtv049", 1, 9, "采昌影劇台", "采昌影劇台", "電影戲劇"),
            ("台灣戲劇台", "litv-xinchuang22", 10003, 20000, "台灣戲劇台", "台灣戲劇台", "電影戲劇"),
            ("影迷數位紀實台", "litv-ftv15", 1, 7, "影迷數位紀實台", "影迷數位紀實台", "科教紀實"),
            ("達文西頻道", "4gtv-4gtv018", 1, 7, "達文西頻道", "達文西頻道", "科教紀實"),
            ("Classica-古典樂", "4gtv-4gtv059", 1, 7, "Classica-古典樂", "Classica古典樂", "科教紀實"),
            ("Mezzo-Live", "4gtv-4gtv083", 1, 6, "Mezzo-Live", "MezzoLive", "科教紀實"),
            ("豬哥亮歌廳秀", "4gtv-4gtv006", 1, 10, "豬哥亮歌廳秀", "豬哥亮歌廳秀", "綜藝娛樂"),
            ("Trace-Urban", "4gtv-4gtv082", 1, 7, "Trace-Urban", "TraceUrban", "體育競技"),
            ("韩国娱乐台KMTV", "4gtv-4gtv016", 1, 7, "韩国娱乐台KMTV", "韓國娛樂台", "綜藝娛樂"),
            ("Arirang-TV", "4gtv-4gtv079", 1, 8, "Arirang-TV", "ArirangTV", "新聞財經"),
            ("MCE", "litv-ftv10", 1, 7, "MCE", "MCE 我的歐洲電影", "電影戲劇"),
            ("第1商业台", "4gtv-4gtv104", 1, 7, "第1商业台", "第1商業台", "新聞財經"),
            ("Pet-Club-TV", "4gtv-4gtv110", 1, 6, "Pet-Club-TV", "Pet Club TV", "科教紀實"),
            ("Smart-知識台", "litv-xinchuang19", 10003, 20000, "Smart-知識台", "Smart知識台", "科教紀實"),
            ("視納華仁紀實頻道", "4gtv-4gtv013", 1, 7, "視納華仁紀實頻道", "視納華仁紀實頻道", "科教紀實"),
            ("客家電視台", "4gtv-4gtv043", 1, 7, "客家電視台", "客家電視台", "綜合頻道"),
            ("好消息", "litv-ftv16", 1, 6, "好消息", "好消息", "綜合頻道"),
            ("好消息2台", "litv-ftv17", 1, 6, "好消息2台", "好消息2台", "綜合頻道"),
            ("國會頻道1", "4gtv-4gtv084", 1, 7, "國會頻道1", "國會頻道1", "科教紀實"),
            ("國會頻道2", "4gtv-4gtv085", 1, 6, "國會頻道2", "國會頻道2", "科教紀實"),
            ("民視", "4gtv-4gtv155", 1, 7, "民視", "民視", "綜合頻道"),
            ("中视经典", "4gtv-4gtv080", 1, 8, "中视经典", "中視經典台", "綜藝娛樂"),
            ("中視菁采台", "4gtv-4gtv064", 1, 9, "中視菁采台", "中視菁采台", "綜藝娛樂"),
            ("中天亚洲", "4gtv-4gtv109", 1, 9, "中天亚洲", "中天亞洲台", "綜合頻道"),
            ("TVBS", "4gtv-4gtv073", 1, 6, "TVBS", "TVBS", "綜合頻道"),
            ("TVBS新闻", "4gtv-4gtv072", 1, 6, "TVBS新闻", "TVBS新聞台", "新聞財經"),
            ("台視", "4gtv-4gtv066", 1, 6, "台視", "台視", "綜合頻道"),
            ("台視新聞台", "4gtv-4gtv051", 1, 6, "台視新聞台", "台視新聞台", "新聞財經"),
            ("台視財經台", "4gtv-4gtv056", 1, 6, "台視財經台", "台視財經台", "新聞財經"),
            ("博斯运动1", "litv-xinchuang07", 10003, 20000, "博斯运动1", "博斯運動一台", "體育競技"),
            ("博斯运动1", "litv-xinchuang08", 10003, 20000, "博斯运动1", "博斯運動二台", "體育競技"),
            ("博斯无限", "litv-xinchuang10", 10003, 20000, "博斯无限", "博斯無限台", "體育競技"),
            ("博斯无限2", "litv-xinchuang13", 10003, 20000, "博斯无限2", "博斯無限二台", "體育競技"),
            ("博斯网球", "litv-xinchuang09", 10003, 20000, "博斯网球", "博斯網球台", "體育競技"),
            ("博斯高球1", "litv-xinchuang05", 10003, 20000, "博斯高球1", "博斯高球台", "體育競技"),
            ("博斯高球2", "litv-xinchuang06", 10003, 20000, "博斯高球2", "博斯高球二台", "體育競技"),
            ("博斯魅力", "litv-xinchuang04", 10003, 20000, "博斯魅力", "博斯魅力台", "體育競技"),
            ("非凡新聞台", "4gtv-4gtv010", 1, 7, "非凡新聞台", "非凡新聞台", "新聞財經"),
            ("非凡商業台", "4gtv-4gtv048", 1, 7, "非凡商業台", "非凡商業台", "新聞財經"),
            ("VOA-美國之音", "litv-ftv03", 1, 7, "VOA-美國之音", "VOA美國之音", "新聞財經"),
        ]

        # 按照原始Py代码格式生成M3U列表
        result = ['#EXTM3U']
        for channel in channels:
            # PHP数据格式: name, channel_id, qlt, alt, logo_name, display_name, group
            name, channel_id, qlt, alt, logo_name, display_name, group = channel
            
            # 生成URL - 保持Py代码原有格式
            # 注意：原Py代码使用的是proxy://格式，但输出的是http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=...格式
            # 这里保持原Py代码的逻辑，但URL中的pid使用PHP的频道ID和参数
            url = f'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid={channel_id},{qlt},{alt}'
            if self.extend:
                url += f'&data={self.extend}'
            
            # 生成EXTINF行 - 保持原Py代码格式
            # 使用PHP数据中的display_name作为显示名称
            # 注意：原Py代码中logo使用的是https://logo.doube.eu.org/，但PHP代码使用的是https://epg.iill.top/logo/
            # 这里保持原Py代码格式，但使用PHP的logo_name
            logo_url = f'https://epg.iill.top/{logo_name}.png'
            result.append(f'#EXTINF:-1 tvg-id="{display_name}" tvg-name="{display_name}" tvg-logo="{logo_url}" group-title="{group}",{display_name}')
            result.append(url)
        
        return '\n'.join(result)

    def homeContent(self, filter):
        return {}

    def homeVideoContent(self):
        return {}

    def categoryContent(self, cid, page, filter, ext):
        return {}

    def detailContent(self, did):
        return {}

    def searchContent(self, key, quick, page='1'):
        return {}

    def searchContentPage(self, keywords, quick, page):
        return {}

    def playerContent(self, flag, pid, vipFlags):
        return {}

    def localProxy(self, params):
        if params['type'] == "m3u8":
            return self.proxyM3u8(params)
        if params['type'] == "ts":
            return self.get_ts(params)
        return [302, "text/plain", None, {'Location': 'https://sf1-cdn-tos.huoshanstatic.com/obj/media-fe/xgplayer_doc_video/mp4/xgplayer-demo-720p.mp4'}]
    
    def proxyM3u8(self, params):
        pid = params['pid']
        info = pid.split(',')
        a = info[0]  # 频道ID
        b = info[1]  # 视频参数qlt
        c = info[2]  # 音频参数alt
        
        # 使用PHP代码中的时间计算：timestamp = int(time.time() / 4 - 355017628)
        timestamp = int(time.time() / 4 - 355017628)
        t = timestamp * 4
        m3u8_text = f'#EXTM3U\n#EXT-X-VERSION:3\n#EXT-X-TARGETDURATION:4\n#EXT-X-MEDIA-SEQUENCE:{timestamp}\n'
        
        for i in range(10):
            # 使用PHP代码中的URL格式
            url = f'https://ntd-tgc.cdn.hinet.net/live/pool/{a}/litv-pc/{a}-avc1_6000000={b}-mp4a_134000_zho={c}-begin={t}0000000-dur=40000000-seq={timestamp}.ts'
            
            if self.is_proxy:
                # 使用base64编码并生成外部代理URL格式
                encoded_url = self.b64encode(url)
                url = f'http://127.0.0.1:9978/proxy?do=py&type=ts&url={encoded_url}'
                if self.extend:
                    url += f'&data={self.extend}'

            m3u8_text += f'#EXTINF:4,\n{url}\n'
            timestamp += 1
            t += 4
        
        return [200, "application/vnd.apple.mpegurl", m3u8_text]

    def get_ts(self, params):
        url = self.b64decode(params['url'])
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, stream=True, proxies=self.proxy)
        return [206, "application/octet-stream", response.content]

    def destroy(self):
        return '正在Destroy'

    def b64encode(self, data):
        return base64.b64encode(data.encode('utf-8')).decode('utf-8')

    def b64decode(self, data):
        return base64.b64decode(data.encode('utf-8')).decode('utf-8')


if __name__ == '__main__':
    pass
```

