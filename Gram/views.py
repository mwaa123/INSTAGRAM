# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect,get_object_or_404
from .models import Image,Comment
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

def welcome(request):
    
        return render(request,'fold/welcome.html')


def gram(request):
        context ={
             'images':Image.objects.all()
        }
    
        return render(request,'fold/gram.html',context)
class ImageListView(ListView):
    model = Image
    template_name = 'fold/gram.html'
    context_object_name = 'images'
    ordering = ['-date_posted']

class ImageDetailView(DetailView):
    model = Image

    
class ImageCreateView(LoginRequiredMixin, CreateView):
    model = Image
    fields = ['title', 'caption','img']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class ImageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Image
    fields = ['title', 'caption','img']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        image = self.get_object()
        if self.request.user == image.user:
            return True
        return False


class ImageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Image
    success_url = '/'

    def test_func(self):
        image = self.get_object()
        if self.request.user == image.user:
            return True
        return False


def search_results(request):
    if 'search_user' in request.GET and request.GET["search_user"]:
        search_term = request.GET.get("search_user")
        searched_users = User.objects.filter(username__icontains=search_term)
        message=search_term

        return render(request,"Gram/search.html", {"images":searched_users, "message":message}) 


    else:
        message = "Search term not found"  

        return render(request,'Gram/search.html',{"message":message})

class CommentCreateView(LoginRequiredMixin,CreateView):
     
    model = Comment
    fields = ['review','image','user']
    success_url = ('/')

    def form_valid(self,form):
      
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)



# class ImageLikeRedirectView(RedirectView):
#     def get_redirect_url(self,pk, *args, **kwargs):
#         obj = get_object_or_404(Image, pk = pk)
#         url= obj.get_absolute_url()
      
#         user = self.request.user
#         if user.is_authenticated:
#             if user in obj.likes.all():
#                 obj.likes.remove(user)
#                 status =''
#             else:
#                 obj.likes.add(user)
#                 status='red'
#         return url