from django.conf import settings
from .views import ImageListView,ImageDetailView,ImageCreateView,ImageDeleteView,ImageUpdateView,CommentCreateView,ImageLikeRedirectView
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
from django.urls import path
urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^gram/',ImageListView.as_view(),name = 'gram'),
    url('^$',views.welcome,name = 'welcome'),
    path('image/<int:pk>/',ImageDetailView.as_view(),name='detail'),
    url('image/new/', ImageCreateView.as_view(), name='image-create'),
    path('image/<int:pk>/update/', ImageUpdateView.as_view(), name='image-update'),
    path('image/<int:pk>/delete/', ImageDeleteView.as_view(), name='image-delete'),
    path('search/',views.search_results, name = 'search_results'), 
    path('image/<int:pk>/comment/',CommentCreateView.as_view(),name = 'comment-create'),
    path('image/<int:pk>/like/',ImageLikeRedirectView.as_view(),name = 'image-likes'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
