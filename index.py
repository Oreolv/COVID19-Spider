import json
import time
import requests

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
# 腾讯疫情实时数据数据 URL
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d' % int(
    time.time() * 1000)
data = json.loads(requests.get(url=url, headers=headers).json()['data'])
