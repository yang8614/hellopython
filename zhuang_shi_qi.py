#coding=utf-8
import urllib2,urllib,re,json,requests,time,lxml,sys
from bs4 import BeautifulSoup

def timer(hello):
    start_1 = time.time()
    hello()
    end_1 = time.time()
    total_time = end_1 - start_1
    print "total_time:"+str((round(total_time,2)))

@timer #装饰器
def hello():
    print('hello')
    time.sleep(2)
    print('world!')


hello   #调用
