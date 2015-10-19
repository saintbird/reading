#coding=utf-8

from django.db import models

# Create your models here.
    
class MainTag(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name

    
class SubTag(models.Model):
    name = models.CharField(max_length=30)
    parent = models.ForeignKey(MainTag)
    
    def __unicode__(self):
        return self.name

class BookInfo(models.Model):
    title = models.CharField(max_length=30)
    rates = models.CharField(max_length=10)
    votes = models.CharField(max_length=10)
    imgUrl = models.CharField(max_length=50)
    tag = models.CharField(max_length=10)
    author = models.CharField(max_length=30)
    authorIntro = models.CharField(max_length=1000)
    summary = models.CharField(max_length=1000)
    price = models.CharField(max_length=10)
    
    def __unicode__(self):
        return self.title