#coding=utf-8
import urllib2,urllib,re,json,requests,time,thread

start = raw_input('请输入起始页码')
end = raw_input('请输入结束页码')
print '开始下载'
time_start= time.time()

def catch(imgelist):
    for i_1 in imgelist:
        reg1 = r'\w{9,16}\.jpg'
        reg_1_imge = re.compile(reg1)
        imge_name = reg_1_imge.findall(i_1)
        for imge_name_1 in imge_name:
            i_2='https:'+i_1
            urllib.urlretrieve(i_2,'/Users/yangkai/PycharmProjects/picture/%s' % imge_name_1)
            print '/Users/yangkai/PycharmProjects/picture/%s............done' % (imge_name_1)

for page_number in range(int(start),int(end)):
    target_url = 'https://www.qiushibaike.com/imgrank/page/%s/' % page_number
    page_html = requests.get(target_url)
    reg = r'//.+\/medium\/.+\.jpg'
    reg_imge = re.compile(reg)
    imgelist = reg_imge.findall(page_html.text)
    thread.start_new_thread(catch,(imgelist,))

time_end = time.time()
time_result = time_end-time_start
catch(imgelist)

print '\n'
print '完成下载,耗时%.2f秒' % time_result


