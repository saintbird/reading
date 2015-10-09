#coding=utf-8

from django.db import models

# Create your models here.
class BookInfo(models.Model):
    title = models.CharField(max_length=30)
    rates = models.CharField(max_length=10)
    votes = models.CharField(max_length=10)
    imgUrl = models.CharField(max_length=50)
    tag = models.CharField(max_length=10)
    author = models.CharField(max_length=30)
    authorIntro = models.CharField(max_length=1000)
    summary = models.CharField(max_length=1000)
    
    def __unicode__(self):
        return self.title
    