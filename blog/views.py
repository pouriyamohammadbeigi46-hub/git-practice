from django.shortcuts import render
from blog.models import Post

def blog_views (request):
    return render ( request,'blog/blog_view.html')

def blog_single (request):
    return render  ( request,'blog/blog_single.html')

def test (request):
    return render (request,'test.html')
