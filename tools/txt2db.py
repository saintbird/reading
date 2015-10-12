#!/usr/bin/env python
#coding:utf-8
 
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "reading.settings")
 
import django
django.setup()
 
def txt2db():
    from book_recommend.models import BookInfo
    f = open('tools/小说')
    BookList = []
    for line in f:
        fieldList = line.split('#$')
        print len(fieldList)
        print "fff"
        title,rates,votes,imgUrl,tag,detailUrl,intro = line.split('#$')
        book = BookInfo(title=title,rates=rates,votes=votes,imgUrl=imgUrl,tag=tag,detailUrl=detailUrl,intro=intro)
        BookList.append(book)
    f.close()
    BookInfo.objects.bulk_create(BookList)

if __name__ == "__main__":
    txt2db()
    print('Done!')