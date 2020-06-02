# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from users.models import Profile

class Image(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    caption = models.TextField()
    img = models.ImageField(upload_to='gala/',blank=True)
    date_posted = models.DateTimeField(default=timezone.now) 
    likes = models.ManyToManyField(User, blank = True, related_name ='image_likes')
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE,null=True)
    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    
    image =models.ForeignKey(Image, related_name = 'image_comments',on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review= models.TextField()

    def __str__(self):
        return self.review