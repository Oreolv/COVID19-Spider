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

china_data = {"add": {}, "total": {}}
province_data = {}

# 提取国内疫情所需数据
for item in data:
    need_key = [
        'confirm', 'dead', 'nowConfirm', 'importedCase', 'noInfect',
        'localConfirm'
    ]
    for item in need_key:
        china_data['add'][item] = data['chinaAdd'][item]
        china_data['total'][item] = data['chinaTotal'][item]

# 解析现有省市有数据
# for item in data['areaTree'][0]['children']:
#     areaItem = {}
#     areaItem.update(name=item['name'],
#                     today=item['today'],
#                     total=item['total'],
#                     children=[])
#     for i in item['children']:
#         if (i['total']['nowConfirm']) > 0:
#             areaItem['children'].append(i)
#     province_data.append(areaItem)

# with open('areaTree.json', 'w', encoding='utf-8') as f:
#     f.write(json.dumps(province_data, ensure_ascii=False))
