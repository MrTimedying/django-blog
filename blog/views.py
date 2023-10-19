from django.shortcuts import render
from .models import Post
from django.views import generic
from taggit.models import Tag



# This two class based views are for the list of articles and the full article display

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'article.html'


# This part is for the meta/tags type of fetching that a visitor can do

class TagList(generic.ListView):
    model = Post
    template_name = 'searched.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get("tag_slug"))