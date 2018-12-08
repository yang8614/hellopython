#coding=utf-8
import urllib2,urllib,re,json,requests,time,lxml,sys
from bs4 import BeautifulSoup
import threading,csv
reload(sys)                   #将python2的编码从ascii改为utf8
sys.setdefaultencoding('utf-8')


#beautifulsoup用法示例说明
html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>'
'''
soup = BeautifulSoup(html,'lxml')
#print soup.prettify()
print soup.title
#<title>The Dormouse's story</title>

print soup.title.name
#title

print soup.title.string
#The Dormouse's story

print soup.title.parent.name
print '1:',soup.p['class']
print '2:',soup.p['name']
print '3:',soup.b
print '4:',soup.b.string
print '5:',soup.find_all('p')[1].a.string
print '6:',soup.find(id = 'link3')['href']
n = 7
for link in soup.find_all('a'):
    print str(n) + ':',link['href']
    n+=1
print "===================="
print soup.find(id = 'link3').string
print soup.get_text()
for a in soup.find_all('a'):
    print a.attrs