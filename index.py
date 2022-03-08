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
province_data = []
city_data = []
province_temp_data = []

# 提取省市疫情所需临时数据
for item in data['areaTree'][0]['children']:
    province_data_item = {}
    province_data_item.update(name=item['name'],
                              today=item['today'],
                              total=item['total'],
                              children=[])
    for i in item['children']:
        if ("grade" in i['total'] and i['total']['nowConfirm'] > 0):
            province_data_item['children'].append(i)
    province_temp_data.append(province_data_item)

with open('province_temp_data.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(province_temp_data, ensure_ascii=False))

# 提取国内疫情所需数据
for item in data:
    need_key = [
        'confirm', 'dead', 'nowConfirm', 'importedCase', 'noInfect',
        'localConfirm'
    ]
    for item in need_key:
        china_data['add'][item] = data['chinaAdd'][item]
        china_data['total'][item] = data['chinaTotal'][item]

with open('china_data.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(china_data, ensure_ascii=False))

# 提取省疫情所需数据
for item in province_temp_data:
    province_data.append({
        "name": item['name'],
        "nowConfirm": item['total']['nowConfirm'],
        "confirm": item['total']['confirm'],
        "heal": item['total']['heal'],
        "dead": item['total']['dead'],
    })

with open('province_data.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(province_data, ensure_ascii=False))

# 提取市疫情所需数据
for p in province_temp_data:
    city_data_item = []
    for c in p['children']:
        city_data_item.append({
            "name": c['name'],
            "province": p['name'],
            "confirm": c['today']['confirm'],
            "nowConfirm": c['total']['nowConfirm'],
            "grade": c['total']['grade'],
        })
    if (len(city_data_item) > 0):
        city_data.append(city_data_item)

with open('city_data.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(city_data, ensure_ascii=False))
