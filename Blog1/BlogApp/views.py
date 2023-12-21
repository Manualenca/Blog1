from urllib import request
from django import forms
from django.shortcuts import get_object_or_404, redirect, render

#from Blog1.form_comments import CommentForm
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

def detalle(request, slug):
    post = get_object_or_404(Post, slug = slug)

    return render(request, 'BlogApp/post_detail.html', {'post': post})
'''if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()'''
    
    