#coding=utf-8

from django.template import loader,Context
from django.http import HttpResponse
from book_recommend.models import BookInfo
from book_recommend.models import SubTag
from django.core.paginator import Paginator, InvalidPage, EmptyPage

# Create your views here.
def douban(request,tag):
    tagList = SubTag.objects.filter(parent=1)
    
    bookList = BookInfo.objects.filter(tag=tag)
    page_size=14
    paginator = Paginator(bookList, page_size)
    try:
        page = int(request.GET.get('page','1'))
    except ValueError:
        page = 1
     
    try:
        books = paginator.page(page)
    except (EmptyPage, InvalidPage):
        books = paginator.page(paginator.num_pages)         
     
    t = loader.get_template("douban.html")
    c = Context({'books':books,'tagList':tagList,'url_tag':tag})
    return HttpResponse(t.render(c))

def famous(request,tag):
    t = loader.get_template('famous.html')
    return HttpResponse(t.render())

def subjects(request,tag):
    t = loader.get_template('subjects.html')
    return HttpResponse(t.render())

def foreign(request,tag):
    t = loader.get_template('foreign.html')
    return HttpResponse(t.render())
