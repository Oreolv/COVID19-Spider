import json
import util
import time
import requests
from lxml import etree

old_data = util.read_json_data('tips_list')


def get_tips(type):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE',
    }
    url = 'https://sa.sogou.com/new-weball/api/sgs/epi-protection/list?type=' + type
    data = requests.get(url=url, headers=headers).json()['list']
    return data


def transform_tips_data():
    type_list = ['chunyun', 'jujia', 'waichu', 'kexue']
    all_data = []
    for i in type_list:
        data = get_tips(i)
        for j in data:
            item = {}
            item['tipsId'] = j['id']
            item['type'] = i
            item['title'] = j['q']
            item['source'] = j['source']
            item['sourceURL'] = j['linkUrl']
            item['publisher'] = 6  #默认发布用户
            item['publishTime'] = j['timestamp']
            all_data.append(item)
        print(i + '分类数据获取成功，此分类添加' + str(len(data)) + '条数据')
    print('所有分类数据获取成功，共添加' + str(len(all_data)) + '条数据')
    return all_data
