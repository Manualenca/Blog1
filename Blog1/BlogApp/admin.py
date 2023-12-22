from django.contrib import admin
from django import forms
from .models import Post, Category, Comment, PostCategory
from django.views.generic.edit import CreateView


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

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'color')
    list_filter = ('name', 'color')
    search_fields = ('name', 'descripcion')
    fields = ('name', 'description', 'color')

admin.site.register(Comment)
admin.site.register(PostCategory)

class PostCategoryInline(admin.TabularInline):
    model = PostCategory
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','created_at','update_at', 'status')
    list_filter = ('status', 'created_at', 'update_at')
    readonly_fields = ('created_at', 'update_at')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'
    ordering = ('created_at',)
    inlines = [PostCategoryInline,]
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Post', {
            'fields':('title', 'content', 'slug', 'status', 'image', 'reporter')
        }),
    )