#coding=utf-8

from django.template import loader,Context
from django.http import HttpResponse
from book_recommend.models import BookInfo
from django.core.paginator import Paginator, InvalidPage, EmptyPage

# Create your views here.
def index(request):
    t = loader.get_template('book_recommend.html')
    return HttpResponse(t.render())

def pages(request,tag):
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
     
    t = loader.get_template("book_cat.html")
    c = Context({'books':books})
    return HttpResponse(t.render(c))
