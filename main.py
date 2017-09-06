from __future__ import print_function
from cloudxns import api
import requests
import re
import json

DOMAIN_ID = ''
HOST = ''
API_KEY = ''
SECRET_KEY = ''

def my_ip():
    raw = requests.get('http://ip.cn', headers={'User-Agent': 'curl/7.54.0'}).text
    return re.findall(r'[\d\.]+', raw)[0]

def main():
    xns = api.Api(API_KEY, SECRET_KEY)
    record_list = json.loads(xns.record_list(DOMAIN_ID))
    for record in record_list['data']:
        if record['host'] != HOST:
            continue
        current = my_ip()
        if record['value'] != current:
            xns.record_update(record['record_id'], DOMAIN_ID, HOST, my_ip(), ttl= 60)
            print('DNS updated')
        else:
            print('Same with original')

if __name__ == '__main__':
    main()
