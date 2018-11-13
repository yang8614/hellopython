#coding=utf-8
import urllib2,urllib,re,json,requests,time,lxml,sys
from bs4 import BeautifulSoup
import threading,csv
reload(sys)                   #将python2的编码从ascii改为utf8
sys.setdefaultencoding('utf-8')

#爬取豆瓣电影top250，中电影评分9.5以上的影片

top_movie_list =[]
url_1 = 'http://api.douban.com/v2/movie/top250?start='
for number in range(0,250,20):
    url_3 = url_1 + str(number)
    req = requests.get(url_3)
    content = req.json()
    subjects = content['subjects']
    for movie in subjects:
        movie_1 = movie['rating']
        movie_2 = movie['genres']
        if movie_1['average'] >=9.0:
            top_movie_list.append([movie['title'],movie_1['average'],movie_2[0]])
            print movie['title'],movie_1['average'],movie_2[0]


with open('douban_movie.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['电影名', '电影评分','电影类型'])
    for data in top_movie_list:
        writer.writerow(data)
