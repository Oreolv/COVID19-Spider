import util
import requests
from lxml import etree


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
        if ('stream' in i['info']):
            continue
        item['newsId'] = i['base']['newsId']
        item['title'] = i['info']['title']
        item['summary'] = i['info']['intro']
        item['sourceURL'] = i['base']['base']['url']
        item['infoSource'] = i['info']['mediaInfo']['name']
        item['publishTime'] = i['info']['showTime']
        ret.append(item)
    return ret


def get_news_content(data):
    for i in data:
        headers = {
            'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.69 Safari/537.36'
        }
        response = requests.get(i['sourceURL'], headers=headers)
        selector = etree.HTML(response.text)
        content = selector.xpath(
            '//section[@class="art_pic_card art_content"]')
        new_content = []
        for j in content[0].xpath('*'):
            if (j.tag == 'p'):
                new_content.append(j.xpath('string(.)'))
            if (j.tag == 'a'):
                url = 'https://' + j.xpath('//img/@data-src')[0]
                new_content.append('<img src="' + url + '"')
        new_content = '\n'.join(new_content).replace('\t', '').replace(
            '\r', '').replace('\n\n', '')
        i['content'] = new_content
    return data


