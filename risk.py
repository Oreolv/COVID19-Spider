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


def get_risk_area():
    timestamp = get_timestamp()
    headers = get_risk_headers(timestamp)
    payload = get_risk_payload(timestamp)
    url = "http://103.66.32.242:8005/zwfwMovePortal/interface/interfaceJson"
    data = requests.post(url, headers=headers, json=payload)
    response_json = data.json()
    return response_json