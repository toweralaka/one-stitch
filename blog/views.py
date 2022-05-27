from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.utils import timezone

from blog.models import Blog


class BlogListView(ListView):
    queryset = Blog.objects.order_by('-publication_date')
    context_object_name = 'blog_list'
    template_name = 'blog/index.html'


class BlogDetailView(DetailView):
    queryset = Blog.objects.all()
    template_name = 'blog/blog_detail.html'

    def get_object(self):
        obj = super().get_object()
        # Record the last accessed date
        obj.views += 1
        obj.last_accessed = timezone.now()
        obj.save()
        return obj

