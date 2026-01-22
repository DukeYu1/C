
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 脚本生成时间：2026-01-23 04:00:20
# 转换为Python版本 - 输出格式为代理URL形式

import time
import urllib.parse
from flask import Flask, request, Response, stream_with_context
import requests

app = Flask(__name__)

# 频道数据
n = {
    # 以下参数为脚本每4小时自动生成一次
    "4gtv-4gtv002": [1, 11, "民視", "綜合頻道", "民視"],
    "4gtv-4gtv003": [1, 7, "民視第一台", "綜合頻道", "民視第一台"],
    "litv-ftv13": [1, 7, "民視新聞台", "新聞財經", "民視新聞台"],
    "4gtv-4gtv001": [1, 7, "民視台灣台", "綜合頻道", "民視台灣台"],
    "litv-ftv09": [1, 6, "民視影劇台", "電影戲劇", "民視影劇台"],
    "litv-ftv07": [1, 6, "民視旅遊台", "科教紀實", "民視旅遊台"],
    "4gtv-4gtv004": [1, 9, "民視綜藝台", "綜藝娛樂", "民視綜藝台"],
    "4gtv-4gtv040": [1, 7, "中视", "綜合頻道", "中視"],
    "4gtv-4gtv074": [1, 6, "中视新闻", "新聞財經", "中視新聞台"],
    "4gtv-4gtv009": [2, 9, "中天新闻", "新聞財經", "中天新聞台"],
    "4gtv-4gtv041": [1, 7, "華視", "綜合頻道", "華視"],
    "4gtv-4gtv052": [1, 6, "華視新聞", "新聞財經", "華視新聞"],
    "4gtv-4gtv046": [1, 7, "靖天綜合台", "綜合頻道", "靖天綜合台"],
    "4gtv-4gtv063": [1, 8, "靖天國際台", "綜合頻道", "靖天國際台"],
    "4gtv-4gtv058": [1, 9, "靖天戲劇台", "電影戲劇", "靖天戲劇台"],
    "4gtv-4gtv047": [1, 2, "靖天日本台", "綜合頻道", "靖天日本台"],
    "4gtv-4gtv055": [1, 9, "靖天映畫台", "電影戲劇", "靖天映畫台"],
    "4gtv-4gtv044": [1, 7, "靖天卡通台", "卡通動漫", "靖天卡通台"],
    "4gtv-4gtv062": [1, 9, "靖天育樂台", "綜藝娛樂", "靖天育樂台"],
    "4gtv-4gtv065": [1, 9, "靖天資訊台", "新聞財經", "靖天資訊台"],
    "4gtv-4gtv061": [1, 7, "靖天電影台", "電影戲劇", "靖天電影台"],
    "4gtv-4gtv054": [1, 9, "靖天歡樂台", "綜藝娛樂", "靖天歡樂台"],
    "litv-xinchuang12": [10003, 20000, "龍華偶像台", "電影戲劇", "龍華偶像台"],
    "litv-xinchuang01": [10002, 20000, "龍華卡通台", "卡通動漫", "龍華卡通台"],
    "litv-xinchuang18": [10003, 20000, "龍華戲劇台", "電影戲劇", "龍華戲劇台"],
    "litv-xinchuang11": [10003, 20000, "龍華日韓台", "電影戲劇", "龍華日韓台"],
    "litv-xinchuang21": [10003, 20000, "龍華經典台", "電影戲劇", "龍華經典台"],
    "litv-xinchuang03": [10003, 20000, "龍華電影台", "電影戲劇", "龍華電影台"],
    "litv-xinchuang02": [10003, 20000, "龍華洋片台", "電影戲劇", "龍華洋片台"],
    "4gtv-4gtv045": [1, 7, "靖洋戲劇台", "電影戲劇", "靖洋戲劇台"],
    "4gtv-4gtv057": [1, 7, "靖洋卡通-Nice-Bingo", "卡通動漫", "靖洋卡通NiceBingo"],
    "litv-longturn14": [1, 6, "寰宇新聞台", "新聞財經", "寰宇新聞台"],
    "4gtv-4gtv156": [1, 8, "寰宇新聞台灣台", "新聞財經", "寰宇新聞台灣台"],
    "4gtv-4gtv158": [1, 2, "寰宇財經台", "新聞財經", "寰宇財經台"],
    "4gtv-4gtv068": [1, 8, "TVBS欢乐", "綜藝娛樂", "TVBS歡樂台"],
    "4gtv-4gtv067": [1, 9, "TVBS精采", "綜藝娛樂", "TVBS精采台"],
    "4gtv-4gtv034": [1, 7, "八大精彩台", "綜藝娛樂", "八大精彩台"],
    "4gtv-4gtv039": [1, 6, "八大綜藝台", "綜藝娛樂", "八大綜藝台"],
    "4gtv-4gtv070": [1, 9, "ELTA娛樂", "綜藝娛樂", "ELTA娛樂台"],
    "litv-xinchuang20": [10003, 20000, "ELTA生活英語", "科教紀實", "ELTV生活英語"],
    "4gtv-4gtv152": [1, 7, "东森新闻", "新聞財經", "東森新聞"],
    "4gtv-4gtv153": [1, 6, "东森财经", "新聞財經", "東森財經新聞"],
    "4gtv-4gtv075": [1, 6, "鏡電視新聞台", "新聞財經", "鏡電視新聞台"],
    "4gtv-4gtv076": [1, 7, "亞洲旅遊台", "科教紀實", "亞洲旅遊台"],
    "4gtv-4gtv053": [1, 9, "GINX-Esports-TV", "體育競技", "GINXEsportsTV"],
    "4gtv-4gtv014": [1, 6, "时尚运动X", "體育競技", "時尚運動X"],
    "4gtv-4gtv101": [1, 6, "智林体育", "體育競技", "智林體育台"],
    "4gtv-4gtv077": [1, 5, "TraceSports", "體育競技", "TraceSports"],
    "4gtv-4gtv011": [1, 7, "影迷數位電影台", "電影戲劇", "影迷數位電影台"],
    "4gtv-4gtv017": [1, 7, "AMC-最愛電影", "電影戲劇", "AMC電影台"],
    "4gtv-4gtv042": [1, 7, "公視戲劇台", "電影戲劇", "公視戲劇台"],
    "4gtv-4gtv049": [1, 9, "采昌影劇台", "電影戲劇", "采昌影劇台"],
    "litv-xinchuang22": [10003, 20000, "台灣戲劇台", "電影戲劇", "台灣戲劇台"],
    "litv-ftv15": [1, 7, "影迷數位紀實台", "科教紀實", "影迷數位紀實台"],
    "4gtv-4gtv018": [1, 7, "達文西頻道", "科教紀實", "達文西頻道"],
    "4gtv-4gtv059": [1, 7, "Classica-古典樂", "科教紀實", "Classica古典樂"],
    "4gtv-4gtv083": [1, 6, "Mezzo-Live", "科教紀實", "MezzoLive"],
    "4gtv-4gtv006": [1, 10, "豬哥亮歌廳秀", "綜藝娛樂", "豬哥亮歌廳秀"],
    "4gtv-4gtv082": [1, 7, "Trace-Urban", "體育競技", "TraceUrban"],
    "4gtv-4gtv016": [1, 7, "韩国娱乐台KMTV", "綜藝娛樂", "韓國娛樂台"],
    "4gtv-4gtv079": [1, 8, "Arirang-TV", "新聞財經", "ArirangTV"],
    "litv-ftv10": [1, 7, "MCE", "電影戲劇", "MCE 我的歐洲電影"],
    "4gtv-4gtv104": [1, 7, "第1商业台", "新聞財經", "第1商業台"],
    "4gtv-4gtv110": [1, 6, "Pet-Club-TV", "科教紀實", "Pet Club TV"],
    "litv-xinchuang19": [10003, 20000, "Smart-知識台", "科教紀實", "Smart知識台"],
    "4gtv-4gtv013": [1, 7, "視納華仁紀實頻道", "科教紀實", "視納華仁紀實頻道"],
    "4gtv-4gtv043": [1, 7, "客家電視台", "綜合頻道", "客家電視台"],
    "litv-ftv16": [1, 6, "好消息", "綜合頻道", "好消息"],
    "litv-ftv17": [1, 6, "好消息2台", "綜合頻道", "好消息2台"],
    "4gtv-4gtv084": [1, 7, "國會頻道1", "科教紀實", "國會頻道1"],
    "4gtv-4gtv085": [1, 6, "國會頻道2", "科教紀實", "國會頻道2"],

    # 如遇到音视频参数变动，需手动修改以下数字部分
    "4gtv-4gtv155": [1, 7, "民視", "綜合頻道", "民視"],
    "4gtv-4gtv080": [1, 8, "中视经典", "綜藝娛樂", "中視經典台"],
    "4gtv-4gtv064": [1, 9, "中視菁采台", "綜藝娛樂", "中視菁采台"],
    "4gtv-4gtv109": [1, 9, "中天亚洲", "綜合頻道", "中天亞洲台"],
    "4gtv-4gtv073": [1, 6, "TVBS", "綜合頻道", "TVBS"],
    "4gtv-4gtv072": [1, 6, "TVBS新闻", "新聞財經", "TVBS新聞台"],
    "4gtv-4gtv066": [1, 6, "台視", "綜合頻道", "台視"],
    "4gtv-4gtv051": [1, 6, "台視新聞台", "新聞財經", "台視新聞台"],
    "4gtv-4gtv056": [1, 6, "台視財經台", "新聞財經", "台視財經台"],
    "litv-xinchuang07": [10003, 20000, "博斯运动1", "體育競技", "博斯運動一台"],
    "litv-xinchuang08": [10003, 20000, "博斯运动1", "體育競技", "博斯運動二台"],
    "litv-xinchuang10": [10003, 20000, "博斯无限", "體育競技", "博斯無限台"],
    "litv-xinchuang13": [10003, 20000, "博斯无限2", "體育競技", "博斯無限二台"],
    "litv-xinchuang09": [10003, 20000, "博斯网球", "體育競技", "博斯網球台"],
    "litv-xinchuang05": [10003, 20000, "博斯高球1", "體育競技", "博斯高球台"],
    "litv-xinchuang06": [10003, 20000, "博斯高球2", "體育競技", "博斯高球二台"],
    "litv-xinchuang04": [10003, 20000, "博斯魅力", "體育競技", "博斯魅力台"],
    "4gtv-4gtv010": [1, 7, "非凡新聞台", "新聞財經", "非凡新聞台"],
    "4gtv-4gtv048": [1, 7, "非凡商業台", "新聞財經", "非凡商業台"],
    "litv-ftv03": [1, 7, "VOA-美國之音", "新聞財經", "VOA美國之音"],
}


def get_curl(url: str, download: bool = False):
    """
    模拟PHP的curl函数
    """
    try:
        if download:
            # 流式下载
            response = requests.get(url, stream=True, verify=False, timeout=30)
            response.raise_for_status()
            
            def generate():
                for chunk in response.iter_content(chunk_size=128000):
                    if chunk:
                        yield chunk
            
            return generate()
        else:
            response = requests.get(url, verify=False, timeout=30, allow_redirects=True)
            response.raise_for_status()
            return response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None


def creat_m3u8(id: str, qlt: int, alt: int, proxy: str) -> str:
    """
    生成m3u8播放列表
    """
    timestamp = int(time.time() / 4 - 355017628)
    t = timestamp * 4
    m3u8 = "#EXTM3U\n"
    m3u8 += "#EXT-X-VERSION:3\n"
    m3u8 += "#EXT-X-TARGETDURATION:4\n"
    m3u8 += f"#EXT-X-MEDIA-SEQUENCE:{timestamp}\n"
    
    for i in range(10):
        m3u8 += "#EXTINF:4,\n"
        ts_url = f"https://ntd-tgc.cdn.hinet.net/live/pool/{id}/litv-pc/{id}-avc1_6000000={qlt}-mp4a_134000_zho={alt}-begin={t}0000000-dur=40000000-seq={timestamp}.ts"
        
        if proxy != "true":
            m3u8 += ts_url + "\n"
        else:
            # 修改为代理URL格式
            base_url = request.host_url.rstrip('/')
            m3u8 += f"{base_url}proxy?do=py&type=ts&url={urllib.parse.quote(ts_url)}\n"
        
        timestamp += 1
        t += 4
    
    return m3u8


def creat_m3u(channels: dict, proxy: str) -> str:
    """
    生成M3U播放列表 - 输出为代理URL格式
    """
    m3u = '#EXTM3U x-tvg-url="https://epg.iill.top/epg.xml.gz"\n'
    base_url = request.host_url.rstrip('/')
    
    for channel_id, channel_info in channels.items():
        qlt = channel_info[0]
        alt = channel_info[1]
        channel_name = channel_info[4]
        group = channel_info[3]
        logo_id = channel_info[2]
        
        # 生成代理URL格式
        if proxy == "true":
            # 如果需要代理，使用代理URL
            proxy_url = f"{base_url}proxy?do=py&type=m3u8&pid={channel_id},{qlt},{alt}"
        else:
            # 直接播放
            proxy_url = f"{base_url}?do=py&type=m3u8&pid={channel_id},{qlt},{alt}"
        
        # 输出M3U格式
        m3u += f'#EXTINF:-1 tvg-id="{channel_id}" tvg-name="{channel_name}" '
        m3u += f'tvg-logo="https://epg.iill.top/logo/{logo_id}.png" '
        m3u += f'group-title="{group}",{channel_name}\n'
        m3u += f'{proxy_url}\n'
    
    return m3u


@app.route('/', methods=['GET'])
def index():
    """
    主路由 - 生成M3U播放列表
    """
    proxy = request.args.get('proxy', '').strip()
    
    return Response(
        creat_m3u(n, proxy),
        mimetype='audio/x-mpegurl',
        headers={'Content-Disposition': 'inline; filename=playlist.m3u'}
    )


@app.route('/proxy', methods=['GET'])
def proxy_handler():
    """
    代理路由 - 处理代理请求
    """
    do_type = request.args.get('do', '').strip()
    content_type = request.args.get('type', '').strip()
    pid = request.args.get('pid', '').strip()
    url = request.args.get('url', '').strip()
    
    if do_type != 'py':
        return Response('Invalid request', status=400, mimetype='text/plain')
    
    if content_type == 'm3u8':
        # 处理m3u8请求
        if not pid:
            return Response('Missing pid parameter', status=400, mimetype='text/plain')
        
        # 解析pid参数：channel_id,qlt,alt
        pid_parts = pid.split(',')
        if len(pid_parts) != 3:
            return Response('Invalid pid format', status=400, mimetype='text/plain')
        
        channel_id = pid_parts[0]
        qlt = int(pid_parts[1])
        alt = int(pid_parts[2])
        
        # 检查频道是否存在
        if channel_id not in n:
            return Response('Channel not found', status=404, mimetype='text/plain')
        
        # 生成m3u8
        m3u8_content = creat_m3u8(channel_id, qlt, alt, "false")
        
        return Response(
            m3u8_content.strip(),
            mimetype='application/vnd.apple.mpegurl',
            headers={'Content-Disposition': 'inline; filename=index.m3u8'}
        )
    
    elif content_type == 'ts':
        # 处理ts片段请求
        if not url:
            return Response('Missing url parameter', status=400, mimetype='text/plain')
        
        # 解码URL
        ts_url = urllib.parse.unquote(url)
        
        # 流式传输TS片段
        def generate():
            stream_gen = get_curl(ts_url, download=True)
            if stream_gen:
                for chunk in stream_gen:
                    yield chunk
        
        return Response(
            stream_with_context(generate()),
            mimetype='video/MP2T',
            headers={
                'Content-Disposition': 'inline; filename=stream.ts',
                'X-Accel-Buffering': 'no',
                'Cache-Control': 'no-cache'
            }
        )
    
    else:
        return Response('Invalid type parameter', status=400, mimetype='text/plain')


@app.route('/m3u8', methods=['GET'])
def m3u8_handler():
    """
    直接m3u8路由 - 兼容旧格式
    """
    channel_id = request.args.get('id', '').strip()
    proxy = request.args.get('proxy', '').strip()
    
    if not channel_id:
        return Response('Missing id parameter', status=400, mimetype='text/plain')
    
    if channel_id not in n:
        return Response('Channel not found', status=404, mimetype='text/plain')
    
    qlt = n[channel_id][0]
    alt = n[channel_id][1]
    
    # 生成m3u8
    m3u8_content = creat_m3u8(channel_id, qlt, alt, proxy)
    
    return Response(
        m3u8_content.strip(),
        mimetype='application/vnd.apple.mpegurl',
        headers={'Content-Disposition': 'inline; filename=index.m3u8'}
    )


if __name__ == '__main__':
    # 可以自定义端口
    port = 9978
    print(f"服务启动在: http://127.0.0.1:{port}")
    print(f"主播放列表: http://127.0.0.1:{port}/")
    print(f"频道示例: http://127.0.0.1:{port}/proxy?do=py&type=m3u8&pid=litv-ftv10,1,7")
    print(f"TS片段代理: http://127.0.0.1:{port}/proxy?do=py&type=ts&url=encoded_url")
    
    app.run(debug=True, host='0.0.0.0', port=port)
```

