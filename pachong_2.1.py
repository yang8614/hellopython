#coding=utf-8
import urllib2,urllib,re,json,requests,time,lxml,sys
from bs4 import BeautifulSoup
#下载 www.pixabay.com 网站首页图片
print '开始下载'
time_start= time.time()                                 #记录开始下载时间
url = 'https://pixabay.com/'
req = requests.get(url)
content = req.text#查看url文本
soup = BeautifulSoup(content,'lxml')
#print soup.prettify()                                  #查看网站树形结构
try:
    for link in soup.find_all('img'):                   #获取img标签地址
        link_1 = link.get('src')                        #获取每个img标签地址中的src属性链接
        reg = '\w+-\w+'                                 #定义提取图片名称用的正则表达式
        reg_imge = re.compile(reg)                      #将正则存储为reg_imge规则
        imge_name = reg_imge.findall(link_1)            #使用reg_imge规则findall，link_1中的图片名称列表
        for imge_name_1 in imge_name:                   #提取图片名称列表中的每一个图片名称
            urllib.urlretrieve(link_1, '../picture/%s.jpg' % imge_name_1)#下载link_1（图片地址链接），存储在picture文件夹，命名为提取的图片名称
            print 'picture %s.jpg.....ok' % imge_name_1 #打印下载成功的图片名称
except:
    print 'download error'
time_end = time.time()                                  #记录结束下载时间
time_result = time_end-time_start                       #使用结束时间-开始时间，计算实际用时
print '完成下载,耗时%.2f秒' % time_result