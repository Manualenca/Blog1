from django.views.generic import UpdateView, CreateView
from django import forms 
from django.shortcuts import get_object_or_404, redirect, render
#from .forms import EditarForm


from .models import Post, Category


# Create your views here.


class CrearPostView (CreateView):
    model = Post
    fields = ['reporter','title','content','categories', 'status', 'image','created_at']
    labels ={
        'reporter': 'Publicador',
        'title': 'Titulo',
        'content': 'Contenido',
        'categories': 'Categoria',
        'status': 'Estado', 
        'image': 'Imagen',
        'created_at': 'Fecha de Creación',
        
    }
    widgets = {
        'reporter': forms.Select(attrs={'class': 'form-contorl'}),
        'title': forms.TextInput(attrs={'class': 'form-contorl'}),
        'content': forms.Textarea(attrs={'class': 'form-contorl'}),
        'categories': forms.Select(attrs={'class': 'form-contorl'}),
        'status': forms.Select(attrs={'class': 'form-contorl'}),
        'image': forms.ClearableFileInput(attrs={'class': 'form-contorl'}),
        'created_at':forms.DateInput(attrs={'class': 'form-control', 'readonly': True}),
    }


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


'''class DetallePostView(UpdateView):
   model = Post
   form_class = EditarForm 
   template_name = 'BlogApp/post_edit.html'
   

    def GuardarModificacion(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        status = request.POST.get('status')
        Post.objects.create(title = title, content = content, status = status)
        return redirect("GuardarModificacion")
    return render(request,'BlogApp/posts.html')
   '''
