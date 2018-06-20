from django.shortcuts import render, get_object_or_404
from .models import BlogPost

# Create your views here.

def blogs(request):
    title = 'Blog'
    posts = BlogPost.objects.all
    return render(request, 'blog/blogs.html', {'title': title, 'posts':posts})

def single(request, blog_id):
    post = get_object_or_404(BlogPost, pk=blog_id)
    title = "Post"
    return render(request, 'blog/single.html', {'post': post, 'title': title})