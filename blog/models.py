# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone

class Categories(models.Model):
    title = models.CharField(max_length=40, null=False )
    
    def __str__(self):
        return str(self.title)

    class Admin:
    	pass

class TagModel(models.Model):
    title = models.CharField(max_length=20, null=False )
    class Admin:
    	pass
    

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    Category = models.ForeignKey(Categories)
    Tags = models.ManyToManyField(TagModel)
    photo = models.ImageField(blank=True, null=True) 
    
    class Admin:
    	   pass

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
        
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
