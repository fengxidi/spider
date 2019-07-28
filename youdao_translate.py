# -*- coding: utf-8 -*-
#-*- author:guozheng -*-

import time
import random
import hashlib
import requests
import json

from urllib import parse


def translate(content):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    #有道反爬虫机制破解
    client = 'fanyideskweb'
    ctime = int(time.time() * 1000)
    salt = str(ctime + random.randint(1, 10))
    key = "n%A-rKaT5fb[Gy?;N5@Tj"
    sign = hashlib.md5((client + content + salt + key).encode('utf-8')).hexdigest()

    formdata = {
        'i': content,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'ts': ctime,
        'bv': 'bbb3ed55971873051bc2ff740579bb49',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION',
        "typoResult": "false"
    }

    data = parse.urlencode(formdata).encode('utf-8')

    headers={
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection':'keep-alive',
        'Content-Length': str(len(data)),  #data的长度
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=411053782.2048327; OUTFOX_SEARCH_USER_ID="624807543@10.169.0.82"; _ga=GA1.2.1183990434.1545953795; __guid=204659719.4171092601073212000.1556529398259.1892; _ntes_nnid=b614992f9793567677715722dca65105,1556529398655; JSESSIONID=aaaYNk4iiiuIx_lAGG2Ww; monitor_count=19; ___rl__test__cookies=1564304579270',
        'DNT': '1',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }


    response = requests.post(url, data=formdata, headers=headers).text

    result = json.loads(response)
    if 'translateResult' in result:
        try:
            result = result['translateResult'][0][0]['tgt']
            print('\033[1;35m {} \033[0m'.format(result))
        except:
            pass

    return None

if __name__ == '__main__':
    while True:
        content = input('请输入需要翻译的内容:')
        print('翻译结果:',end="")
        translate(content)







