# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

# Create your views here.
def welcome(request):
    
    return render(request,'fold/welcome.html')