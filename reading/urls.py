"""reading URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',  'reading.views.index', name='home'),
    url(r'^about$',  'reading.views.about', name='about'),
    url(r'^feedback$',  'reading.views.feedback', name='feedback'),
    url(r'^douban/(.+)/$', 'book_recommend.views.douban', name='douban'),
    url(r'^famous/(.+)/$', 'book_recommend.views.famous', name='famous'),
    url(r'^sujects/(.+)/$', 'book_recommend.views.subjects', name='subjects'),
    url(r'^foreign/(.+)/$', 'book_recommend.views.douban', name='foreign'),
]
