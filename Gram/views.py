# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import Image
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

# Create your views here.
def welcome(request):
    
    return render(request,'fold/welcome.html')


def gram(request):
    context ={
        'images':Image.objects.all()
    }
    
    return render(request,'fold/gram.html',context)
