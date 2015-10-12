#coding=utf-8

import urllib2
from bs4 import BeautifulSoup
import codecs
import json
import sys
import os
import django

reload(sys)
sys.setdefaultencoding('utf8')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "../reading.settings")
django.setup()
        
def get_book_info_from_page(tag,url):
    print url
    exception_file = codecs.open("exception", 'a+','utf-8')

    try:
        obj = urllib2.urlopen(url)
        html = obj.read()
        obj.close()
        soup = BeautifulSoup(html)
        booklist = soup.find_all("dl")
    except Exception,e:
        exception_file.write("except1"+"\n" + url+"\n"+str(e)+"\n")
        return "exception"

    if len(booklist) == 0:
        return "finish"
    
    ret = ""
    i = 0
    for book in booklist:
        i = i+1
        try:
            book_rates = book.select("span.rating_nums")[0].text
        except Exception,e:
            exception_file.write("except2:"+str(i)+"\n"+url+"\n"+str(e)+"\n")
            continue

        if float(book_rates)>8.4:
            book_detail_url = book.select("a")[0]["href"]
            print book_detail_url
            try:
                obj2 = urllib2.urlopen(book_detail_url)
                book_detail = obj2.read()
                obj2.close()
                book_detail_soup = BeautifulSoup(book_detail)
                img_url = book_detail_soup.select("a.nbg")[0]["href"]
                title = book_detail_soup.select("a.nbg")[0]["title"]
                votes = book_detail_soup.find("span",{"property": "v:votes"}).string
                intro_list = book_detail_soup.select("div.intro")
                if len(intro_list) != 3:
                    intro = intro_list[0].text
                else:
                    intro = intro_list[1].text
                if long(votes)>100:
                    ret = ret +title +'#$' +book_rates + '#$' +votes + '#$' +img_url+'#$' +tag +'#$'+book_detail_url+'#$'+intro+'\n'
            except Exception,e:
                exception_file.write("except3"+"\n"+book_detail_url+"\n"+str(e)+"\n")
                continue
    exception_file.close()
    return ret
            
def get_book_info_from_api(tag,url):
    print url
    exception_file = codecs.open("exception", 'a+','utf-8')
    ret = ""
    BookList = []
    #try:
    obj = urllib2.urlopen(url)
    html = obj.read()
    obj.close()
    js = json.loads(html)
    if js["count"] == 0:
        ret  = "finish"
    else:
        for i in range(0,len(js["books"])):
            book = BookInfo(title=js["books"][i]["title"], 
                        rates=str(js["books"][i]["rating"]["average"]),
                        votes=str(js["books"][i]["rating"]["numRaters"]),
                        imgUrl=js["books"][i]["image"],
                        tag=tag,
                        author=js["books"][i]["author"],
                        author_intro = js["books"][i]["author_intro"],
                        summary=js["books"][i]["summary"])
            BookList.append(book)
        BookInfo.objects.bulk_create(BookList)
    #except Exception,e:
        #exception_file.write(url+"\n"+str(e)+"\n")
        #ret = "exception"
        
    exception_file.close()
    return ret
            
if __name__ == '__main__':
    #base_url = "http://www.douban.com/tag/tag_name/book?start="
    base_url = "https://api.douban.com/v2/book/search?tag=tag_name&start="
    tag_list_wenxue = ["小说",]
    tag_list_jingguan = ["经济学","管理",	"经济","金融","商业","投资","营销","理财","创业","广告","股票","企业史","策划"]
   
    for tag in tag_list_wenxue:
        tmp_url = base_url.replace("tag_name",tag)

        for i in range(0,2):
            url = tmp_url + str(i*20)
            ret = get_book_info_from_api(tag,url)
            if ret =="finish":
                print "finish"
                break
            
