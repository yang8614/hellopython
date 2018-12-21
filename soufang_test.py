#coding=utf-8
import urllib2,urllib,re,json,requests,time,lxml,sys
from bs4 import BeautifulSoup
import threading,csv
from lxml import etree
reload(sys)                   #将python2的编码从ascii改为utf8
sys.setdefaultencoding('utf-8')


#使用selenium 搭配 chrmoe无头模式(headless),爬取搜房网房屋图片信息
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()#配置chrome无头模式
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

str = '闵行'
str_1 = str.decode('UTF-8')

url = "http://sh.zu.fang.com/"
driver = webdriver.Chrome(chrome_options=chrome_options)#创建driver网页驱动器
driver.set_window_size(1920,10000)#设置截取屏幕大小
driver.get(url)#请求网页
time.sleep(1)#等待1秒
driver.find_element_by_id('input_key').send_keys(str_1)#定位输入框，输入"闵行"
driver.find_element_by_id('closecover').click()#点击页面遮罩"确定"按钮
driver.find_element_by_id('rentid_39').click()#点击搜索按钮

for i in range(5):
    content = driver.page_source#获取页面信息
    tree = etree.HTML(content)#页面信息变为树形结构，方便使用xpath
    result = tree.xpath('//dl[@class = "list hiddenMap rel"]')#获取帖子区域

    for info in result:#从帖子区域中提取每个组件
        try:
            rent = info.xpath('.//span[@class="price"]')[0]#定位价格位置
            #print rent
            rent_1 = rent.xpath('string()')#获取文本信息

            house_name = info.xpath('.//p[@class="gray6 mt12"]')[0]#定位房子名称
            house_name_1 = house_name.xpath('string()')#获取文本信息
            #print rent_1,house_name_1


            picture_name = info.xpath('.//img[@class = "b-lazy b-loaded"]/@src')[0]#定位图片链接
            picture_name_1 = picture_name.split('/')[-2]#获取链接中的图片编码
            img_name = rent_1 + '-' + house_name_1 + picture_name_1#组合图片名称：价格+房子名称+图片编码
            print img_name#输出图片名称

            img = info.xpath('.//img[@class = "b-lazy b-loaded"]/@src')[0]#获取图片地址
            img_url = 'https:' + img#组合图片地址为可下载链接
            urllib.urlretrieve(img_url, '../picture/%s.jpg' % img_name)#下载图片到python文件上一级菜单中叫picture的文件夹

        except:
            print "----无信息----"

    driver.find_element_by_link_text('下一页').click()#完成上述动作后点击进入下一页，再次重复上述动作
    print '翻到下一页'

print 'done'
