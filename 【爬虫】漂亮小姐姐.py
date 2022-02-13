# 用到的技术点
# 1.requests发送请求
# 2.BeautifulSoup来解析整个页面源代码 -> 特简单

from ast import Break, IsNot, Str
from email import header
from json.tool import main
import os
from pickle import NONE
from wsgiref import headers
import requests
from bs4 import BeautifulSoup 

# 爬取网站的第一件事，发送请求
request = requests.get('http://www.umeitu.com/meinvtupian/meinvxiezhen/')
request.encoding = 'utf-8'

# 解析html
main_page = BeautifulSoup(request.text,'html.parser')
# 从页面中找到某些东西
# find()  找到一个可以点击的
# find_all() 找到所有可以点击的东西
alist = main_page.find('div',attrs = {'class':'TypeList'}).find_all('a',attrs = {'class':'TypeBigPics'})
n = 0
for a in alist:
    n += 1
    m = 1
    href = 'https://www.umeitu.com/' + a.get('href')
    # 发送请求到子页面，进入到有小姐姐的页面中
    resp1 = requests.get(href, timeout=5)
    resp1.encoding = 'utf-8'
    child_page = BeautifulSoup(resp1.text,'html.parser')
    # 找到图片的真实路径
    src = child_page.find('div',attrs = {'class':'ImageBody'}).find('img').get('src')
    # 发送请求到服务器，把图片下载下来
    f = open(f'D:\\python_workplace\\【爬虫】漂亮小姐姐\\tu_%s.jpg' % str(n),mode = 'wb')
    if(os.path.lexists(f'D:\\python_workplace\\【爬虫】漂亮小姐姐\\tu_%s' % str(n))):
        os.remove(f'D:\\python_workplace\\【爬虫】漂亮小姐姐\\tu_%s' % str(n))
    f.write(requests.get(src).content)
    print(href + '    已经下载好了！')
    for i in range(2,100):
        m += 1
        Href2 = []
        Href1 = str(href)
        Href2 = Href1.split(".")
        Href2[0] = Href2[0] + '.'
        Href2[1] = Href2[1] + '.'
        Href2[-2] = Href2[-2] + f'_{m}.'
        Href2 = [str(i) for i in Href2]
        Href1 = ''.join(Href2)
        try:
            # 发送请求到子页面，进入到有小姐姐的页面中
            resp1 = requests.get(Href1)
            resp1.encoding = 'utf-8'
            child_page = BeautifulSoup(resp1.text,'html.parser')
            # 找到图片的真实路径
            src = child_page.find('div',attrs = {'class':'ImageBody'}).find('img').get('src')
            # 发送请求到服务器，把图片下载下来
            f = open(f'D:\\python_workplace\\【爬虫】漂亮小姐姐\\tu_{n}_{m}.jpg',mode = 'wb')
            f.write(requests.get(src).content)
            print(Href1 + '    已经下载好了！')
        except NameError:
            break
        except AttributeError:
            break
print('全部下载完毕！！')

    

