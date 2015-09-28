from django.template import loader,Context
from django.http import HttpResponse
from book_recommend.models import BookInfo

# Create your views here.
def index(request):
    books = BookInfo.objects.all()
    t = loader.get_template('book_recommend.html')
    c = Context({'books':books})
    return HttpResponse(t.render(c))
