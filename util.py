import json
import hashlib


def write_json(dir, data):
    with open('../Guard-Server/static/{}.json'.format(dir),
              'w',
              encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False))


def get_sha256_str(data):
    str = hashlib.sha256(data.encode('utf-8')).hexdigest()
    return str