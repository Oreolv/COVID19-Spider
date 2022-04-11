import os
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
    if (not os.path.isfile('../Guard-Server/static/{}.json'.format(dir))):
        write_json(dir, [])
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
    if (len(str(time_stamp))):
        time_stamp = int(time_stamp / 1000)
    time_array = time.localtime(time_stamp)
    str_date = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    return str_date


def get_mysql_connection():
    conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db='guard',
        charset='utf8',
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute('SET CHARACTER SET utf8;')
    return conn, cursor
