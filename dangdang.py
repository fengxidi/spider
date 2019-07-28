
# coding: utf-8

import ssl
import requests
import re
import json
import pandas



#爬取当当网高评分书籍

#请求数据
def request_dandan(url):

    try:
        response = requests.get(url)
        if response.status_code == 200:
          
            return response.text
    except requests.RequestException:
        return None





def parse_result(html):

    pattern = re.compile('<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?target="_blank">(.*?)</a>.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>',re.S)
	
    items = re.findall(pattern,html)  #正则匹配有用数据

    for item in items:
        yield {'range': item[0],'iamge': item[1], 'title': item[2], 'star' :item[3], 'recommend': item[4], 'author': item[5], 'times': item[6], 'price': item[7]}


def write_item_to_file(item):
    print('开始写入数据 ====> ' + str(item))
    with open('book.txt', 'a', encoding='UTF-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
        f.close()


def main(page):
    url = 'http://bang.dangdang.com/books/fivestars/01.22.00.00.00.00-recent30-0-0-1-' + str(page)
    html = request_dandan(url)

    items = parse_result(html) # 解析过滤我们想要的信息
   
    for item in items:
        write_item_to_file(item)

if __name__ == "__main__":
    for i in range(1,26):  #当一页的数据提取完，进入下一页
        main(i)
    print("stop")



##将文本文档该改成表格形式储存（csv）
with open('book.txt', 'r', encoding=('utf-8')) as f:
    data = []
    files = f.readlines()

    for file in files:
        data.append(eval(file))
        
    sourse = pd.DataFrame(data)
    sourse.to_csv("book_data.csv")
 

