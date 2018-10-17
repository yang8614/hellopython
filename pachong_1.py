#coding=utf-8
import urllib2,urllib,re,json,requests,time,thread
from lxml import etree

url = 'http://jandan.net/duan'
data_all = ''
for i in range(3):

    content = requests.get(url)
    #print (content.text)
    content_1 = content.text

    tree = etree.HTML(content_1)
    result = tree.xpath('//li//div[@class="text"]')
    #print result
    for div in result:
        author = div.xpath('../div[@class="author"]/strong/text()')
        data_all += (author[0] + ':\n\n')
        div_1 = div.xpath('p/text()')
        for i_1 in div_1:
            data_all += i_1
        data_all += '\n\n'

    current_page = tree.xpath('//span[@class="current-comment-page"]/text()')
    next_page = int(current_page[0].strip('[]'))-1

    url = 'http://jandan.net/duan/page-%d'% next_page

with open('pachong_1.txt','w') as f:
    data_all_1 = data_all.encode('utf8')
    f.write(data_all_1)