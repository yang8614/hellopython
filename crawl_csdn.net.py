#coding=utf-8
import urllib2,urllib,re,json,requests,time,lxml,sys
from bs4 import BeautifulSoup
import threading,csv
reload(sys)                   #将python2的编码从ascii改为utf8
sys.setdefaultencoding('utf-8')

#爬取csdn网站最新文章页面
url = 'https://www.csdn.net/api/articles?type=more&category=newarticles&shown_offset='
shown_offset = '1541860743000000'
content = []
for i in range(5):
    try:
        req = requests.get(url+shown_offset)
        data = req.json()
        number= data['shown_offset']
        shown_offset = str(number)
        for articles in data['articles']:
            if articles['title'] not in content:
                content.append([articles['user_name'],articles['title'],articles['views']])
    except:
        print('failed')


with open('csdn_articles.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['作者姓名', '文章标题', '文章阅读量'])
    for data in content:
        writer.writerow(data)