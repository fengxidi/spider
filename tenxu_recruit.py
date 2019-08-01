import requests
from  retrying import retry
import time
import json
import pandas as pd

class Tenxu():
    def __init__(self,index, keyword):
        self.index = index
        self.keyword = keyword
        self.url ='https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1564658511102&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=cn'.format(self.keyword,self.index)
        self.headers = {

            'authority': 'careers.tencent.com',
            'method': 'GET',
            'scheme':'https',
            'path' : self.url,
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': '_ga = GA1.2.1487228706.1554171553;pgv_pvi = 1579087872;_gcl_au = 1.1.1663934486.1562311314;__guid = 151231787.1295879711641581800.1564628678559.5645;monitor_count = 22;loading = agree',
            'dnt': '1',
            'referer': 'https://careers.tencent.com/search.html?index={}&keyword={}'.format(self.index,self.keyword),
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',

        }

        self.timestamp = int(time.time()*1000)

        self.formdata = {
            'timestamp': self.timestamp,
            'keyword': self.keyword,
            'pageIndex': self.index,

            'pageSize': 10,
            'language': 'zh-cn',
            'area': 'cn'
        }
    @retry(stop_max_attempt_number=5) #调用retry，当assert出错时候，重复请求5次
    def parse_url(self,url):
        response = requests.get(url,timeout=10,headers=self.headers) #请求url
        print(response.status_code)
        assert response.status_code==200  #当响应码不是200时候，做断言报错处理

        return response.text


    def parse_content(self,data):
        contents = json.loads(data)['Data']['Posts']
        print(type(contents))
        #
        # for content in contents:
        #     # title = content["RecruitPostName"]
        #     # work =
        #     # CountryName = content["CountryName"]
        #     # LocationName=content[LocationName]
        #     # CategoryName = content['CategoryName']
        #     # pub_time =
        #     # Responsibility = content['Responsibility']
        #
        #     print(content)
        #     print(type(content))
        return contents

    def save_file_csv(self,contents):

        if self.index ==0:
            sourse = pd.DataFrame(contents)
            sourse.to_csv('tenxu_recruit_{}.csv'.format(self.index))
        else:
            sourse = pd.read_csv('tenxu_recruit_{}.csv'.format(self.index-1),usecols=[i for i in range(1,16)])
            sourse = sourse.append(contents)
            sourse.to_csv('tenxu_recruit_{}.csv'.format(self.index))
    def run(self):
        soup = self.parse_url(self.url)
        contents = self.parse_content(soup)
        self.save_file_csv(contents)

if __name__ == '__main__':

    keywork = input("输入需要检索的关键词:")
    num =  eval(input("输入需要抓取的职位数量:"))
    for i in range(num//10):
        T  = Tenxu(i,keywork)
        T.run()





