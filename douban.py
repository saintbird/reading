#coding=utf-8

import urllib2
from bs4 import BeautifulSoup
import codecs
import json
import sys
import os
import cookielib
import django
import random
import time

reload(sys)
sys.setdefaultencoding('utf8')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "reading.settings")
django.setup()

from book_recommend.models import BookInfo

def openurl(url):
    """
    打开网页
    """
    cookie_support= urllib2.HTTPCookieProcessor(cookielib.CookieJar())
    opener = urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    user_agents = [
                'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
                'Opera/9.25 (Windows NT 5.1; U; en)',
                'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
                'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
                'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
                'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
                "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
                "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",

                ] 
   
    agent = random.choice(user_agents)
    opener.addheaders = [("User-agent",agent),("Accept","*/*"),('Referer','http://www.google.com')]
    try:
        res = opener.open(url)
    except Exception,e:
        raise Exception
    else:
        return res
    
headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; cn-ZH; rv:1.9.1.6)Gecko/20091201 Firefox/3.5.6'}   
            
def get_book_info_from_api(tag,url):
    print url
    exception_file = codecs.open("exception", 'a+','utf-8')
    ret = ""
    BookList = []
    try:
        req = urllib2.Request(url = url, headers = headers)
        obj = openurl(url)
        html = obj.read()
        obj.close()
        js = json.loads(html)
        if js["count"] == 0:
            ret  = "finish"
        else:
            for i in range(0,len(js["books"])):
                rates=float(js["books"][i]["rating"]["average"])
                votes=js["books"][i]["rating"]["numRaters"]
                if (rates>8.4 and votes>1000) or (rates>8 and votes>10000):
                    authorList=str(js["books"][i]["author"]).replace("\\xb7",".").decode('raw_unicode_escape').split(",")
                    if len(authorList) == 1:
                        author = authorList[0][3:-2]
                    else:
                        author = authorList[0][3:-1]
                    book = BookInfo(bookid=js["books"][i]["id"],
                                isbn10=js["books"][i]["isbn10"],
                                isbn13=js["books"][i]["isbn13"],
                                title=js["books"][i]["title"], 
                                rates=str(js["books"][i]["rating"]["average"]),
                                votes=str(js["books"][i]["rating"]["numRaters"]),
                                imgUrl=js["books"][i]["images"]["large"],
                                tag=tag,
                                author = author,
                                authorIntro = js["books"][i]["author_intro"].replace("\n","<br>"),
                                summary=js["books"][i]["summary"].replace("\n","<br>"),
                                price = js["books"][i]["price"])
                    BookList.append(book)
            BookInfo.objects.bulk_create(BookList)
    except Exception,e:
        exception_file.write(url+"\n"+str(e)+"\n")
        ret = "exception"
        
    exception_file.close()
    return ret
            
if __name__ == '__main__':
    #base_url = "http://www.douban.com/tag/tag_name/book?start="
    base_url = "https://api.douban.com/v2/book/search?tag=tag_name&start="
    tag_list_wenxue = ["小说","历史"]
    tag_list_jingguan = ["心理学","社会学","经济学","管理","金融","互联网","科学"]
   
    for tag in tag_list_wenxue:
        tmp_url = base_url.replace("tag_name",tag)

        for i in range(0,3000):
            url = tmp_url + str(i*20)
            random_time = (int)(random.random()*10)
            print random_time
            time.sleep(random_time)
            ret = get_book_info_from_api(tag,url)
            if ret =="finish":
                print "finish"
                break
            
