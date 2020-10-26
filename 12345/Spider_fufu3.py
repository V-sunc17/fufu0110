import os
os.environ['http_proxy'] = 'http://139.128.244.140:3333'
os.environ['https_proxy'] = 'http://139.128.244.140:3333'
from bs4 import BeautifulSoup
#import urllib2
import requests       #导入requests包
url = 'https://news.163.com/'
#url = 'http://www.easymarketplace.de/online-pdfs.php'
headers={
  'user-agent':'Mozilla/5.0'
}
try:
    strhtml = requests.get(url,headers=headers)        #Get方式获取网页数据
except Exception as err:
    print(f'Other error occurred: {err}')  # Python 3.6

#print(strhtml.text)

soup=BeautifulSoup(strhtml.text,'lxml')  # lxml 'html.parser'

t1 = soup.find_all('a')
href_list = []

#print(t1)

for k in t1:
#    print(k)
#    print(k['class'])#查a标签的class属性
#    print(k['id'])#查a标签的id值
#    print(k['href'])#查a标签的href值
#    print(k.get('href'))
#     print('Level 1@@@@@@@@@@@@@@@@@@@@@')

#     print(k.string)#查a标签的string
     url2=k.get('href')
#     print(t3)
     if url2 == 'http://dy.163.com/article/FM2Q81MA05346936.html' :
         print(k.get('href'))
         try:
            strhtml2=requests.get(url2,headers=headers)
         except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6
         soup2=BeautifulSoup(strhtml2.text,'lxml')
         print(soup2)
         t2 = soup2.find_all('a')

         for k2 in t2:
            print('Level 2')
    #        print(k2.get('href'))
            print(k2.string)#查a标签的string

#     href_list.append(t3)

#print(href_list)
