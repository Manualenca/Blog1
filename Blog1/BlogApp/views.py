from django.shortcuts import get_object_or_404, render,HttpResponse
from .models import Post, Category


# Create your views here.

def inicio(request):

    return render(request,"BlogApp/base.html")

def posts(request):
    posts = Post.objects.all()

    return render (request,'BlogApp/posts.html', {'posts': posts})

def posts_by_category(request, slug):

    category = get_object_or_404(Category, slug=slug)
    posts_in_category = Post.objects.filter(categories=category)
    return render(request, 'BlogApp/posts.html', {'posts': posts_in_category})

