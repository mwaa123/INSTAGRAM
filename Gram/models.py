# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Image(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    caption = models.TextField()
    img= models.ImageField(upload_to='gala/',blank=True)
    date_posted = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.title

 


    
    # comment= models.TextField()
    # prof= models.ForeignKey('Profile',on_delete=models.CASCADE ,null=True )  #profile image




 
# class Profile (models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     bio = models.TextField()
#     img= models.ImageField(default="default.jpg",upload_to='gala/')
#     name = models.TextField( blank=True)
# Create your models here.
