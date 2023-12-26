from urllib import request
from django import forms
from django.shortcuts import get_object_or_404, redirect, render

from .forms.form_blog1 import PostForm

#from Blog1.form_comments import CommentForm
from .models import Post, Category, PostCategory


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


def create_post(request):
    if request.method == 'POST':
        post_form = PostForm.save(commit=False)
        categories = request.POST.getlist('categories')

        if post_form.is_valid():
            new_post = post_form.save(commit= False)
            new_post.save()
            for category_id in categories:
                PostCategory.object.create(post=new_post, category_id=category_id)
            return redirect('Inicio')
    else:
        post_form= PostForm()
        categories = Category.objects.all()

    context = {
                'post_form': post_form,
                'categories': categories
    }
    return render(request,'BlogApp/post_create.html', {'Inicio': posts})
            




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
    
    