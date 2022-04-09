import util
import requests


# 通过新浪新闻获取新闻数据
def get_news():
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }
    url = 'https://feeds.sina.cn/api/v4/tianyi?mod=w2019ncov'
    data = requests.get(url=url, headers=headers).json()['result']['data']
    return data


def transform_news_data(data):
    ret = []
    for i in data:
        item = {}
        item['title'] = i['info']['title']
        item['summary'] = i['info']['intro']
        item['sourceURL'] = i['base']['base']['url']
        item['infoSource'] = i['info']['mediaInfo']['name']
        item['publishTime'] = i['info']['showTime']
        data.append(item)
    return ret

