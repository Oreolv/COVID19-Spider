import json
import util
import time
import requests
from lxml import etree

old_data = util.read_json_data('news_list')


# 通过新浪新闻获取新闻数据
def get_news():
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE',
        "cookie":
        "ustat=__122.192.27.11_1646718701_0.72368000; genTime=1646718701; SINAGLOBAL=545914418108.90594.1648704286110; Apache=9945400743798.418.1649551421671; ULV=1649551421675:4:3:1:9945400743798.418.1649551421671:1649516064562; vt=4; recent_visited=%5B%7B%22t%22%3A1649558254501%2C%22u%22%3A%22https%3A//news.sina.cn/gn/2022-04-10/detail-imcwiwst0934999.d.html%22%7D%2C%7B%22t%22%3A1649564236934%2C%22u%22%3A%22https%3A//news.sina.cn/gn/2022-04-10/detail-imcwipii3376041.d.html%22%7D%2C%7B%22t%22%3A1649566237503%2C%22u%22%3A%22https%3A//news.sina.cn/2022-04-09/detail-imcwipii3329585.d.html%22%7D%2C%7B%22t%22%3A1649566961368%2C%22u%22%3A%22https%3A//news.sina.cn/kfy.d.html%22%7D%2C%7B%22t%22%3A1649577493812%2C%22u%22%3A%22https%3A//news.sina.cn/gn/2022-04-08/detail-imcwipii3097701.d.html%22%7D%5D; historyRecord={'href':'https://news.sina.cn/kfy.d.html','refer':'https://news.sina.cn/gn/2022-04-10/detail-imcwipii3376041.d.html'}"
    }
    params = {
        "action": 0,
        "up": 1,
        "down": 0,
        "length": 20,
        "cre": 'tianyi',
        "mod": 'w2019ncov',
        "static": 1,
        "merge": 3,
        "language": 'zh-CN',
        "cnt": {
            "caller": "crmjs",
            "traceid": "crmjs_" + str(util.get_timestamp)
        },
        "ad": {
            "rotate_count": 4743,
            "page_url":
            "https://news.sina.cn/kfy.d.html?vt=4&ncovArticleEntrance=1",
            "platform": "wap",
            "v": "*",
            "timestamp": util.get_timestamp,
            "net": None,
            "channel": "181473"
        },
        "tm": 1489716199,
    }
    url = 'https://feeds.sina.cn/api/v4/tianyi'
    first_data = requests.get(url=url, headers=headers,
                              params=params).json()['result']['data']
    for i in range(1, 100):
        params['action'] = 1
        params['up'] = i
        url = 'https://feeds.sina.cn/api/v4/tianyi'

        data = requests.get(url=url, headers=headers,
                            params=params).json()['result']['data']
        time.sleep(0.5)
        if (len(data) > 0):
            first_data = first_data + data
            print('获取第' + str(i) + '页数据')
        else:
            print('获取第' + str(i) + '页数据时，所有数据获取完毕')
            break

    return first_data


def transform_news_data(data):
    ret = []
    newsIdList = []
    for i in data:
        item = {}
        if ('stream' in i['info']):
            continue
        item['newsId'] = i['base']['newsId']
        if (i['base']['newsId'] in newsIdList):
            continue
        else:
            newsIdList.append(item['newsId'])
            item['title'] = i['info']['title']
            item['summary'] = i['info']['intro']
            item['sourceURL'] = i['base']['base']['url']
            item['infoSource'] = i['info']['mediaInfo']['name']
            item['publishTime'] = i['info']['showTime']
            ret.append(item)
    return ret


def get_news_content(data):
    for idx, i in enumerate(data):
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
        print('获取第' + str(idx + 1) + '条数据内容成功，标题为' + i['title'])
    data = data + old_data
    return data


def remove_same_data(data):
    for i in data[:]:
        if (i['newsId'] in json.dumps(old_data)):
            data.remove(i)
    print('新增' + str(len(data)) + '条数据')
    return data


def get_news_list():
    data = get_news()
    data = transform_news_data(data)
    data = remove_same_data(data)
    data = get_news_content(data)
    print('所有数据获取完毕')
    return data