#coding=utf-8

import urllib2
from bs4 import BeautifulSoup
import csv
import codecs
        
def write_to_csv():
    with open('douban_books.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(['a', '1', '1', '2', '2'])
        
def write_to_file(file_name,data):
    file_object = codecs.open(file_name, 'w','utf-8')
    file_object.write(data)
    file_object.close( )
    
def add_books():
    bookList = []
    bookList.append(BookInfo(title="滚蛋吧!肿瘤君",rates = "9.3", votes="10879",imgUrl="http://img4.douban.com/lpic/s20742806.jpg",tag=""))
    bookList.append(BookInfo(title="你一生的故事",rates = "9.0", votes="1047",imgUrl="http://img3.douban.com/lpic/s28033064.jpg",tag=""))
    bookList.append(BookInfo(title="百年孤独",rates = "9.2", votes="61296",imgUrl="http://img3.douban.com/lpic/s6384944.jpg",tag=""))
    bookList.append(BookInfo(title="白夜行",rates = "9.1", votes="137860",imgUrl="http://img3.douban.com/lpic/s4610502.jpg",tag=""))
    bookList.append(BookInfo(title="小王子",rates = "9.0", votes="185703",imgUrl="http://img4.douban.com/lpic/s1237549.jpg",tag=""))
    BookInfo.objects.bulk_create(bookList)
        
def get_book_info(url):
    print url
    soup = urllib2.urlopen(url)
    html = soup.read()
    soup = BeautifulSoup(html)
    booklist = soup.find_all("dl")
    ret = ""
    for book in booklist:
        book_rates = book.select("span.rating_nums")[0].text
        if float(book_rates)>8.9:
            book_detail_url = book.select("a")[0]["href"]
            print book_detail_url
            book_detail = urllib2.urlopen(book_detail_url).read()
            book_detail_soup = BeautifulSoup(book_detail)
            img_url = book_detail_soup.select("a.nbg")[0]["href"]
            title = book_detail_soup.select("a.nbg")[0]["title"]
            votes = book_detail_soup.find("span",{"property": "v:votes"}).string
            ret = ret + title +"," + votes + "," + book_rates + "," + img_url + "\n"
    return ret
            
if __name__ == '__main__':
    base_url = "http://www.douban.com/tag/tag_name/book?start=0"
    tag_list = ["小说","诗歌"]
    tag_list_jingguan = ["经济学","管理",	"经济","金融","商业","投资","营销","理财","创业","广告","股票","企业史","策划"]
    for tag in tag_list:
        url = base_url.replace("tag_name",tag)
        ret = get_book_info(url)
        write_to_file(tag,ret)