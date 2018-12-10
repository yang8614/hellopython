#coding=utf-8
import urllib2,urllib,re,json,requests,time,lxml,sys
from bs4 import BeautifulSoup
import threading,csv
from lxml import etree
reload(sys)                   #将python2的编码从ascii改为utf8
sys.setdefaultencoding('utf-8')


#xpath用法示例说明
html_1 = '''
<bookstore>

<book>
  <title lang="eng">Harry Potter</title>
  <price>29.99</price>
</book>

<book>
  <title lang="eng">Learning XML</title>
  <price>39.95</price>
</book>

<book>
  <title lang="aiv">HHHHHHa XML</title>
  <price>39.95</price>
</book>

</bookstore>
'''
tree = etree.HTML(html_1)
content = tree.xpath('//title[@lang ="eng"]/text()')
print content

content_1 = tree.xpath('//bookstore')
print content_1

content_2 = tree.xpath('//book//title/text()')
print content_2

content_3 = tree.xpath('//price/text()')
print content_3

content_4 = tree.xpath('//book//title[@lang="aiv"]/text()')
print content_4

