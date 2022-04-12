import util
import time
import requests
import json


def get_timestamp():
    timestamp = str(int(time.time()))
    return timestamp


def get_header_signature(timestamp):
    token = "fTN2pfuisxTavbTuYVSsNJHetwq5bJvCQkjjtiLM2dCratiA"
    signature = util.get_sha256_str(timestamp + token + timestamp).upper()
    return signature


def get_payload_signature(timestamp, nonceHeader):
    token = "23y0ufFl5YxIyGrI8hWRUZmKkvtSjLQA"
    signatureHeader = util.get_sha256_str(timestamp + token + nonceHeader +
                                          timestamp)
    return signatureHeader


def get_risk_payload(timestamp):
    appId = "NcApplication"
    key = "3C502C97ABDA40D0A60FBEE50FAAD1DA"
    nonceHeader = "123456789abcdefg"
    paasHeader = "zdww"
    timestampHeader = timestamp
    signatureHeader = get_payload_signature(timestampHeader, nonceHeader)
    payload = {
        "appId": appId,
        "key": key,
        "nonceHeader": nonceHeader,
        "paasHeader": paasHeader,
        "signatureHeader": signatureHeader,
        "timestampHeader": timestampHeader
    }
    return payload


def get_risk_headers(timestamp):
    signature = get_header_signature(timestamp)
    nonce = "QkjjtiLM2dCratiA"
    paasid = "smt-application"
    headers = {
        'x-wif-nonce': nonce,
        'x-wif-paasid': paasid,
        'x-wif-signature': signature,
        'x-wif-timestamp': timestamp,
    }
    return headers


def merge_same_province(data):
    province_data = []
    new_data = []
    children_index = 0
    for i in data:
        city_list = []

        if i['province'] not in province_data:
            children_index = 1

            province_data.append(i['province'])
            index = len(province_data)
            city_list.append({
                "id": children_index,
                "city": i['city'],
                "county": i['county'],
                "area_name": i['area_name'],
                "communitys": i['communitys'],
            })
            new_data.append({
                "id": index,
                "province": i['province'],
                'children': city_list
            })
        else:
            children_index = children_index + 1
            index = province_data.index(i['province'])
            city_list.append({
                "id": children_index,
                "city": i['city'],
                "county": i['county'],
                "area_name": i['area_name'],
                "communitys": i['communitys'],
            })
            new_data[index]['children'].append(city_list[0])
    return new_data


def transform_risk_area(data):
    new_data = {}
    highlist = merge_same_province(data['highlist'])
    middlelist = merge_same_province(data['middlelist'])
    new_data['end_update_time'] = data['end_update_time']
    new_data['hcount'] = data['hcount']
    new_data['mcount'] = data['mcount']
    new_data['highlist'] = highlist
    new_data['middlelist'] = middlelist
    return new_data


def add_id_risk_area(data):
    for i in range(len(data['highlist'])):
        data['highlist'][i]['id'] = i
    for i in range(len(data['middlelist'])):
        data['middlelist'][i]['id'] = i
    return data


def get_risk_area():
    timestamp = get_timestamp()
    headers = get_risk_headers(timestamp)
    payload = get_risk_payload(timestamp)
    url = "https://bmfw.www.gov.cn/bjww/interface/interfaceJson"
    data = requests.post(url, headers=headers, json=payload).json()['data']

    last_data = util.read_json_data('risk_area')
    if (len(last_data) > 0
            and last_data['end_update_time'] != data['end_update_time']):
        data['last_hcount'] = last_data['hcount']
        data['last_mcount'] = last_data['mcount']
    else:
        data['last_hcount'] = last_data['last_hcount']
        data['last_mcount'] = last_data['last_hcount']
    # return transform_risk_area(data)
    print('疫情风险地区数据获取成功')
    return add_id_risk_area(data)


def get_risk_area_merge():
    timestamp = get_timestamp()
    headers = get_risk_headers(timestamp)
    payload = get_risk_payload(timestamp)
    url = "http://103.66.32.242:8005/zwfwMovePortal/interface/interfaceJson"
    data = requests.post(url, headers=headers, json=payload).json()['data']

    # return transform_risk_area(data)
    return transform_risk_area(data)