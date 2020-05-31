from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    # url('^profile/',views.profile,name = 'profile'),
    # url('^gram/',views.gram,name = 'gram'),
    # url('^edit/',views.edit,name = 'edit'),
]

