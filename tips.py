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
            item['summary'] = j['a']
            item['source'] = j['source']
            item['sourceURL'] = j['linkUrl']
            item['publisher'] = 6  #默认发布用户
            item['publishTime'] = j['timestamp']
            all_data.append(item)
        print(i + '分类数据获取成功，此分类添加' + str(len(data)) + '条数据')
    print('所有分类数据获取成功，共添加' + str(len(all_data)) + '条数据')
    return all_data


def get_tips_content(data):
    for idx, i in enumerate(data[:]):
        headers = {
            'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.69 Safari/537.36'
        }
        response = requests.get(i['sourceURL'], headers=headers)
        selector = etree.HTML(response.text)
        content = selector.xpath('//div[@class="rd-issue_wrap"]')
        if (len(content) == 0):
            data.remove(i)
            continue
        new_content = []
        for j in content[0].xpath('*'):
            strong = j.xpath('./strong//text()')
            text = j.xpath('string(.)')
            if (len(strong) > 0):
                text = "<div class='title'><strong>" + strong[0].strip(
                ) + "</strong></div>"
                new_content.append(text)
            else:
                p = "<div class='section'>" + text.strip() + "</div>"
            new_content.append(p)

            img = j.xpath('.//img/@data-original-src')
            if (len(img) > 0):
                new_content.append(
                    '<div class="img_div"><img mode="widthFix" src="' +
                    img[0].strip() + '" /></div>')
        new_content = '<br />'.join(new_content).replace('\t', '').replace(
            '\r', '').replace('\n', '')
        i['content'] = new_content
        print('获取第' + str(idx + 1) + '条数据内容成功，标题为' + i['title'])
    return data


def remove_same_data(data):
    for i in data[:]:
        if (i['tipsId'] in json.dumps(old_data)):
            data.remove(i)
    print('新增' + str(len(data)) + '条数据')
    return data


def write_tips_mysql(data):
    sql = 'replace into tips (tipsId, content, source, publisher, publishTime, title, summary, type, sourceURL, createdAt, updatedAt) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
    conn, cursor = util.get_mysql_connection()
    for i in data:
        dt = util.get_strftime()
        cursor.execute(sql,
                       (i['tipsId'], i['content'], i['source'], i['publisher'],
                        util.transform_strftime(i['publishTime']), i['title'],
                        i['summary'], i['type'], i['sourceURL'], dt, dt))
        conn.commit()
        print('插入成功:' + i['title'])
    cursor.close()
    conn.close()


def get_tips_list():
    data = transform_tips_data()
    data = remove_same_data(data)
    data = get_tips_content(data)
    write_tips_mysql(data)
    # 合并数据
    data = data + old_data
    print('所有数据获取完毕')
    return data
