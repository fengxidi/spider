
# coding: utf-8

# In[523]:


import urllib.request
import ssl
import requests
import re
import json
from bs4 import BeautifulSoup


#请求数据
def request_douban(url):
  
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None

#解析数据，提取需要的内容
def analysis(soup):
    
    list = soup.find(class_='grid_view').find_all('li')

    for item in list:
        yield {'名字' : item.find(class_='title').string,
               '海报':item.find('a').find('img').get('src'),
               '评分': item.find(class_='rating_num').string,
               '人数': item.find(class_='star').find_all('span')[3].string,
               '引语':item.find(class_='inq').string
              }
            

#将提取的内容写到video.txt
def write_txt(item):
    print('开始写入数据 ====> ' + str(item))
    with open('video.txt', 'a', encoding='UTF-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
        f.close()


def main(page):
    url = 'https://movie.douban.com/top250?start='+ str(page*25)+ '&filter='
    html = request_douban(url)
    soup = BeautifulSoup(html, 'lxml')
    items = analysis(soup)
    for item in items:
        write_txt(item)

if __name__ == "__main__":
    for i in range(10):
        main(i)
    print("stop")





import pandas as pd

#将文本文档该改成表格（csv）
with open('video.txt', 'r', encoding=('utf-8')) as f:
    data = []
    files = f.readlines()

    for file in files:
        data.append(eval(file))  #这里可以采用json模块来实现eval的作用
        
    sourse = pd.DataFrame(data)
    sourse.to_csv("video_data.csv")

