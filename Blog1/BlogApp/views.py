from urllib import request
from django import forms
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import UpdateView
from .forms import CrearForm

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
        post_form = CrearForm.save(commit=False)
        categories = request.POST.getlist('categories')

        if post_form.is_valid():
            new_post = post_form.save(commit= False)
            new_post.save()
            for category_id in categories:
                PostCategory.object.create(post=new_post, category_id=category_id)
            return redirect('create')
    else:
        post_form= CrearForm()
        categories = Category.objects.all()

    context = {
                'post_form': post_form,
                'categories': categories
    }
    return render(request,'BlogApp/post_create.html', {'post': post_form})
            




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

class DetallePostView(UpdateView):
   model = Post
   form_class = CrearForm 
   template_name = 'BlogApp/post_edit.html'
   

def GuardarModificacion(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        status = request.POST.get('status')
        categories = request.POST.get('categories')

        Post.objects.create(title = title, content = content, status = status, categories = categories)
        return redirect("GuardarModificacion")
    return render(request,'BlogApp/posts.html')

    