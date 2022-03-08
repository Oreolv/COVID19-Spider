import json
import time
import requests


# 通过腾讯疫情获取实时数据数据
def get_data():
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }

    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d' % int(
        time.time() * 1000)
    data = json.loads(requests.get(url=url, headers=headers).json()['data'])
    return data


# 提取省市疫情所需临时数据
def get_temp_data(data):
    province_temp_data = []
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
    return province_temp_data


# 提取国内疫情所需数据
def get_china_data(data):
    china_data = []
    for item in data:
        need_key = [
            'confirm', 'dead', 'nowConfirm', 'importedCase', 'noInfect',
            'localConfirm'
        ]
        for item in need_key:
            china_data.append({'chinaAdd': data['chinaAdd'][item]})
            china_data.append({'chinaTotal': data['chinaTotal'][item]})
    return china_data


# 提取省疫情所需数据
def get_province_data(province_temp_data):
    province_data = []
    for item in province_temp_data:
        province_data.append({
            "name": item['name'],
            "nowConfirm": item['total']['nowConfirm'],
            "confirm": item['total']['confirm'],
            "heal": item['total']['heal'],
            "dead": item['total']['dead'],
        })
    return province_data


# 提取市疫情所需数据
def get_city_data(province_temp_data):
    city_data = []
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
    return city_data


def write_json(dir, data):
    with open('../Barrier-Server/static/{}.json'.format(dir),
              'w',
              encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False))


if __name__ == '__main__':
    data = get_data()
    province_temp_data = get_temp_data(data)
    china_data = get_china_data(data)
    province_data = get_province_data(province_temp_data)
    city_data = get_city_data(province_temp_data)
    write_json('china_data', china_data)
    write_json('province_data', province_data)
    write_json('city_data', city_data)
