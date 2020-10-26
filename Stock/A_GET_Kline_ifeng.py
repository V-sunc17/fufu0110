# fufu F87441C
# fufu 2020/10/23 10:33

import json
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


def download(code):
#    download_url = "http://quotes.money.163.com/service/chddata.html?code=1" + code + "&start=" + start_date + "&end=" + end_date + \
#                   "&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
    download_url = "http://api.finance.ifeng.com/akmin?scode=" + code + "&type=60"
    print(download_url)
    data = requests.get(download_url, headers=headers)
#    print("股票-------股票--------------------------", data)
#    df = pd.DataFrame.from_dict(data, orient='index')
#    print("股票-------股票--------------------------", df)
#    f = open(code + '.csv', 'wb')
    for chunk in data.iter_content(chunk_size=100000):
 #       df = pd.DataFrame.from_dict(chunk, orient='index')
 #       print("股票股票-------股票--------------------------")
        df = chunk.decode('UTF-8')
        df2 = json.loads(df)
        df3 = df2['record']
        df4 = pd.DataFrame(df3, columns =["日期", "开盘价", "最高价", "收盘价", "最低价", "成交量", "价格变动", "涨跌幅", "5日均价", "10日均价", "20日均价", "5日均量", "10日均量", "20日均量", "换手率"])
        df4.to_csv(code + '.csv')
#        if chunk:
#            f.write(chunk)
#        #           print('1股票---', code,  '历史数据正在下载')
        print('股票---', code, '历史数据正在下载')

url = 'http://api.finance.ifeng.com/akmin?scode=sz002230&type=60'
response = parse_url(url)
#code, start_date, end_date = get_date(response)
download('sz002230')


stock = pd.read_csv("sz002230.csv")                  # , encoding='gbk'

export_csv = stock.to_csv(r'D:\users\f87441c\Desktop\sz002230.csv', index=None, header=True, encoding='utf-8-sig')
