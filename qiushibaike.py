#coding=utf-8
import requests
import json
from retrying import retry
from lxml import html
etree = html.etree

class Qiubai_spider():
    def __init__(self):
        self.url = "http://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        }

    @retry(stop_max_attempt_number=5) #调用retry，当assert出错时候，重复请求5次
    def parse_url(self,url):
        response = requests.get(url,timeout=10,headers=self.headers) #请求url
        assert response.status_code==200  #当响应码不是200时候，做断言报错处理
        print(url)
        return etree.HTML(response.text) #返回etree之后的html

    def parse_content(self,html):
        item_temp = html.xpath("//div[@class='recommend-article']/ul/li")
        print(len(item_temp))
        for item in item_temp:
            #print(etree.tostring(item, encoding="utf-8").decode("utf-8"))
            #获取用户头像地址
            #print(item.tag)

            avatar = item.xpath("//img/@src")[1] if len(item.xpath("//img//@src"))>0 else None
            avatar = str(avatar)
            # print(avatar)
            # print(type(avatar))
            #avatar = etree.tostring(avatar, encoding="utf-8").decode("utf-8")

            #为头像地址添加前缀
            if avatar is not None and not avatar.startswith("http:"):
                avatar = "http:"+avatar
            print(avatar)

            name = item.xpath("//span/text()")[5] #获取用户名

            print(name)
            content = item.xpath('//a[@class="recmd-content"]/text()') #获取内容
            print(content)
            star_number = item.xpath("//span/text()")[0] #获取点赞数
            print(star_number)
            comment_number = item.xpath("//span/text()")[3] #获取评论数
            print(comment_number)
            print("*"*100)

            message = {
                'name':name,
                'avatar': avatar,
                'content': content,
                'star_number':star_number,
                'comment_number': comment_number
            }
            yield message
    def writer_json_text(self,message):
        json.dump(message, open('qiushibaike.json','a+', encoding='utf-8'),indent=1,ensure_ascii=False)


    def run(self):
        '''函数的主要逻辑实现
        '''
        url = self.url.format(1) #获取到url
        html = self.parse_url(url) #请求url
        messages = self.parse_content(html) #解析页面内容并把内容存入内容队列
        for message in messages:
            self.writer_json_text(message)

if __name__ == "__main__":
    qiubai = Qiubai_spider()
    qiubai.run()