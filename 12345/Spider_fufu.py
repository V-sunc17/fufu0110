import os
os.environ['http_proxy'] = 'http://139.128.244.140:3333'
os.environ['https_proxy'] = 'http://139.128.244.140:3333'
from bs4 import BeautifulSoup
#import urllib2
import requests       #导入requests包
#url = 'https://news.163.com/'
url = 'http://www.easymarketplace.de/online-pdfs.php'
strhtml = requests.get(url)        #Get方式获取网页数据
#print(strhtml.text)

soup=BeautifulSoup(strhtml.text,'lxml')  # lxml 'html.parser'

t1 = soup.find_all('a')
href_list = []

for t2 in t1:
#    t3 = t2.get('href')
     t4 = t2.text.replace("/", " ", 21)
     t5 = t2.get('href')
     t3 = t5 + ' ' + t4

     if t5.endswith(".pdf"):
 #        downloadPath = 'D:\SAP Doc\Download'
         url = t5
         r = requests.get(url, stream=True)
         print(r.content)
#         req = urllib2.urlopen(r)
         with open("D:/SAP Doc/Download/"+ t4 + ".pdf", 'wb') as f:
             f.write(r.content)

#     print(t3)

#     href_list.append(t3)

#print(href_list)
