
# coding: utf-8

# In[124]:


import urllib.request
import ssl
import requests
import re
import json


# In[4]:


response = urllib.request.urlopen('http://www.baidu.com')


# In[8]:


#response.read().decode("utf-8")


# In[11]:


r = requests.get('https://api.github.com/events')


# In[13]:


#r.text


# In[10]:


r = requests.post('https://httpbin.org/post', data = {'key':'value'})


# In[ ]:






# In[34]:


ss = "Xiaoshuaib has 100 bananas"


# In[36]:


ff ="456sdfgkhdfkgkjfd  大小 poli  hgsdf lsjfdskgsfd"


# In[49]:


text2 = re.search('^.*\s{2}?(.+)\s*.*s$',ff)


# In[50]:


print(text2)


# In[32]:


text1 = re.match("^Xi.*?(\d+)\s.*s$",ss)


# In[33]:


text1.group(1)


# In[27]:


content = 'Xiaoshuaib has 100 bananas'
res = re.match('^Xi.*(\d+)\s.*s$',content)
print(res.group(1))


# ### 爬取当当网高评分书籍

# In[149]:


def request_dandan(url):

    try:
        response = requests.get(url)
        if response.status_code == 200:
          
            return response.text
    except requests.RequestException:
        return None


# In[150]:


def parse_result(html):

    pattern = re.compile('<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?target="_blank">(.*?)</a>.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>',re.S)
    #pattern = re.compile('<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>',re.S)
    items = re.findall(pattern,html)
    #print(items)
    for item in items:
        yield {'range': item[0],'iamge': item[1], 'title': item[2], 'star' :item[3], 'recommend': item[4], 'author': item[5], 'times': item[6], 'price': item[7]}


# In[151]:


def write_item_to_file(item):
    print('开始写入数据 ====> ' + str(item))
    with open('book.txt', 'a', encoding='UTF-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
        f.close()


# In[154]:


def main(page):
    url = 'http://bang.dangdang.com/books/fivestars/01.22.00.00.00.00-recent30-0-0-1-' + str(page)
    html = request_dandan(url)
    #print(html)
    items = parse_result(html) # 解析过滤我们想要的信息
    #print(items)
    for item in items:
     
        write_item_to_file(item)


# In[155]:


if __name__ == "__main__":
    for i in range(1,26):
        main(i)
    print("stop")


# ### 

# In[107]:


ff = func()


# In[109]:


print(ff)
for a in ff:

    print(a)


# In[262]:


with open('book.txt', 'r', encoding=('utf-8')) as f:
    data = []
    files = f.readlines()

    for file in files:
        data.append(eval(file))
        
    sourse = pd.DataFrame(data)
    sourse.to_csv("book_data.csv")
 


# In[172]:


file1 = eval(file)


# In[182]:


file1
type(file1)


# In[175]:


file1.keys()


# In[177]:


import pandas as pd


# In[246]:


se = pd.DataFrame( file1.values(),columns = file1.keys())


# In[240]:


se


# In[234]:


file1


# In[235]:


file1


# In[236]:


se.append([file1])


# In[219]:


data  = pd.DataFrame([{1:9,2:8}])


# In[220]:


data


# In[222]:


data.append([{1:7,2:6}])


# In[225]:


data.append([{1:8,2:3}],[1])


# In[247]:


file


# In[248]:


file1


# In[249]:


data = [file,file1]


# In[250]:


data


# In[251]:


data = pd.DataFrame(data)


# In[252]:


data


# In[253]:


file= str(file)


# In[254]:


file1 = str(file1)


# In[258]:


data = [file,file1]


# In[261]:


data = eval(data)


# In[259]:


data = pd.DataFrame(data)


# In[260]:


data

