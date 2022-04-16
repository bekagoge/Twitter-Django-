from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from  datetime import datetime, date


# Create your models here.

class Tweet(models.Model):
    tweetTitle = models.CharField(max_length=255, null=True, blank=True)
    tweetTitleTag = models.CharField(max_length=255, null=True, blank=True)
    tweetAuthor = models.ForeignKey(User, on_delete=models.CASCADE,  null=True, blank=True)  #if we want to delate User we CASCADE and delate all posts
    tweetText = models.TextField(null=True, blank=True)
    tweetDate = models.DateField(auto_now_add = True)
    tweetCategory = models.CharField(max_length=255, default='twitter')
    

    def __str__(self):
        return str(self.tweetTitle) + ' | ' + str(self.tweetAuthor)


    def get_absolute_url(self):
        #return reverse('PostDetails', args=[str(self.id)] ) 
        return reverse('HomePage') 

    #post tweets 

class Category(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.name)


    def get_absolute_url(self):
        #return reverse('PostDetails', args=[str(self.id)] ) 
        return reverse('HomePage') 