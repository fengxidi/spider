import requests
import json

headers = {

            'method': 'GET',
            'scheme':'https',
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': '_ga = GA1.2.1487228706.1554171553;pgv_pvi = 1579087872;_gcl_au = 1.1.1663934486.1562311314;__guid = 151231787.1295879711641581800.1564628678559.5645;monitor_count = 22;loading = agree',
            'dnt': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',

        }
#url = 'https://www.toutiao.com/api/pc/feed/?category=news_hot'
url = 'https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=10&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true'
#url = 'https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1759DB4B2ABFF9&cp=5D42EB7F9F79AE1&_signature=am9CTgAANzGkBMScmHhYUGpvQl'
response = requests.get(url,headers=headers)
print(response.status_code)
wbdata =  response.text

data = json.loads(wbdata)


news = data['data']
print(len(news))

for n in news:

    img_url =None
    url = None
    title = n['title']

    if 'image_url' in n.keys():
        img_url = n['image_url']
    if "media_url" in n.keys():
        url = n["media_url"]
    print(url,title,img_url)

