import time, json, requests

# 腾讯疫情实时数据数据 URL
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d' % int(
    time.time() * 1000)
data = json.loads(requests.get(url=url).json()['data'])
print(data)
