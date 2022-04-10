import json
import time
import hashlib
import pymysql


def write_json(dir, data):
    with open('../Guard-Server/static/{}.json'.format(dir),
              'w',
              encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False))


def read_json_data(dir):
    with open('../Guard-Server/static/{}.json'.format(dir),
              'r',
              encoding='utf-8') as f:
        data = json.load(f)
    return data


def get_sha256_str(data):
    str = hashlib.sha256(data.encode('utf-8')).hexdigest()
    return str


def get_timestamp():
    return int(round(time.time() * 1000))


def get_strftime():
    time_stamp = int(time.time())
    time_array = time.localtime(time_stamp)
    str_date = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    return str_date


def transform_strftime(time_stamp):
    time_stamp = int(time_stamp)
    time_array = time.localtime(time_stamp)
    str_date = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    return str_date


def write_mysql(data):
    conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db='guard',
        charset='utf8',
    )
    sql = 'insert into news (content, publishTime, title,summary, infoSource, sourceURL, createdAt, updatedAt) values (%s,%s,%s,%s,%s,%s,%s,%s);'
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute('SET CHARACTER SET utf8;')

    for i in data:
        dt = get_strftime()
        cursor.execute(
            sql,
            (i['content'], transform_strftime(i['publishTime']), i['title'],
             i['summary'], i['infoSource'], i['sourceURL'], dt, dt))
        conn.commit()
        print('插入成功:' + i['title'])
    conn.close()
