# fufu F87441C
# fufu 2020/10/23 10:33


import os

import pandas as pd

os.environ['http_proxy'] = 'http://139.128.244.140:3333'
os.environ['https_proxy'] = 'http://139.128.244.140:3333'

import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
}


def parse_url(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return etree.HTML(response.content)
    return False


def get_date(response):
    # 得到股票代码，开始和结束的日期
    start_date = ''.join(response.xpath('//input[@name="date_start_type"]/@value')[0].split('-'))
    end_date = ''.join(response.xpath('//input[@name="date_end_type"]/@value')[0].split('-'))
    code = response.xpath('//h1[@class="name"]/span/a/text()')[0]
    return code, start_date, end_date


def download(code, start_date, end_date):
    download_url = "http://quotes.money.163.com/service/chddata.html?code=1" + code + "&start=" + start_date + "&end=" + end_date + \
                   "&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
    print(download_url)
    data = requests.get(download_url, headers=headers)
    f = open(code + '.csv', 'wb')
    for chunk in data.iter_content(chunk_size=10000):
        if chunk:
            f.write(chunk)
            print('1股票---', code, start_date, end_date, '历史数据正在下载')
    print('股票---', code, '历史数据正在下载')


url = 'http://quotes.money.163.com/trade/lsjysj_002230.html'
response = parse_url(url)
code, start_date, end_date = get_date(response)
download(code, start_date, end_date)

stock = pd.read_csv("002230.csv", encoding='gbk')
# stock.head()
# print(stock)
# Export DataFrame to CSV File
export_csv = stock.to_csv(r'D:\users\f87441c\Desktop\002230_2.csv', index=None, header=True, encoding='utf-8-sig')
