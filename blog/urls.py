from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('article/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('tags/<slug:tag_slug>/', views.TagList.as_view(), name='article_by_tag'),
]