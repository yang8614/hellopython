#coding=utf-8
import urllib2,urllib,re,json,requests,time,lxml,sys
from bs4 import BeautifulSoup
import threading,csv
reload(sys)                   #将python2的编码从ascii改为utf8
sys.setdefaultencoding('utf-8')

url_1 = 'https://www.zhihu.com/api/v4/members/'
url_2 = '/followees?include=data%5B*%5D.answer_count%2Carticles_count' \
      '%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadg' \
      'e%5B%3F(type%3Dbest_answerer)%5D.topics&limit=20&offset='

header ={
'cookie':'_zap=1b7b6216-3680-4207-94e8-49f96bbe537b; __DAYU_PP=3vIMZ2NVmVMQAYq76JmR21797f67e57f; d_c0="ABBjxv_KnQ2PTo7nEBQTWbgp4AXP6mXJaps=|1526707606"; _xsrf=MT4UToHZusEE7Mb1g5Z8bas7dqdGdvPB; q_c1=9b0f4e25f8294e529bb99bb071c61f92|1539879175000|1517244183000; __gads=ID=4f1d524886872300:T=1539879362:S=ALNI_Mbjn3KPrNzV-0rcgc1GinioIV0fuQ; tst=h; __utmz=155987696.1539880255.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); l_n_c=1; l_cap_id="ZjJjZDM5ODg0ZDNkNDI3Zjk2OTlmODEzZTYxMmQ0YzY=|1540654259|3cb5f1efbc181f4b9f7e32a05ffd0e936e7cb080"; r_cap_id="ZjM1MmNhY2Q3MjEzNDU5NWFiMWI2MTcyNjA5OWJlYTc=|1540654259|f3e92291bac754b384eddf4c303a8b041a458f7a"; cap_id="Y2Y2YjA0NTQ0OWZkNGQ4Njg1YmQwOWFiYzQ2Y2E0ZDM=|1540654259|4f6d55bf1c5b4f83ae998125a92999de433b5604"; n_c=1; client_id="ODBDMDJDMDE3NTAyMkE0QTE3MDkwMDEwRjZCMEM1NEI=|1540654278|57c321041f74d222379de984b47173d85e5e695a"; capsion_ticket="2|1:0|10:1540654658|14:capsion_ticket|44:ZjdjZjFhNTdhMzMzNDY3YjlhYWRlMDFiMGFmYmExZTY=|dbea237c30510143ac692205388abf55a24283393ac32e7706efb3c6b7ec3c15"; z_c0=Mi4xazZUdURBQUFBQUFBRUdQR184cWREUmNBQUFCaEFsVk5VZFRCWEFDUFUwRFFheDNGTTc5dVNoNDJpelBVQmsxMVB3|1540654673|5803e73e1e04a7bbea03b706a22187c417cbf929; __utmc=155987696; __utma=155987696.1323522189.1539880255.1540711231.1540716635.3; anc_cap_id=940bb39910b44fa09ba28e07bec8bce1; tgw_l7_route=170010e948f1b2a2d4c7f3737c85e98c',
'referer':'https://www.zhihu.com/people/gary-4-63/following?page=2',
'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
'host':'www.zhihu.com'
}

to_crawl = ['gary-4-63']
crawled = []
finished = threading.Event()
all_user = []

def crawl(url):
      global to_crawl,crawled,finished,all_user
      req = requests.get(url, headers=header)
      data = req.json()

      for user in data['data']:
            if user['follower_count'] > 500000:
                  token = user['url_token']
                  if token not in to_crawl and token not in crawled:
                        print(user['name'])
                        to_crawl.append(token)
                        all_user.append([token,user['name'],user['follower_count'],user['is_following']])
                        finished.set()
      return data['paging']

def get_follower(user):
      print('crawling:', user)
      global to_crawl,crawled,finished
      url = url_1 + user + url_2 + '0'
      paging =  crawl(url)
      totals = paging['totals']
      count = 20
      while count < totals and totals < 100:
            url = url_1 + user + url_2 + str(count)
            t = threading.Thread(target=crawl,args=(url,))
            t.start()
            count += 20
      print('to crawl: ', to_crawl)
      print('crawled: ', crawled)
      print('\n')

while len(to_crawl) > 0:
      user = to_crawl.pop()
      crawled.append(user)
      get_follower(user)
      while len(to_crawl) == 0 and threading.active_count() > 1:
            print (to_crawl)
            print ('wait:',threading.active_count())
            finished.clear()
            finished.wait(3)

with open('zhihu_V.csv','w') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow(['token','昵称','粉丝数','是否关注'])
      for data in all_user:
            writer.writerow(data)
