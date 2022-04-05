import json
import hashlib


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