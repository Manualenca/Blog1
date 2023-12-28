from django.db import models
from django.utils.text import slugify

from UsuarioApp.models import UserModel

# Create your models here.
COLOR_CHOICES = (
    ('1', 'celeste'),
    ('2', 'beige'),
    ('3', 'salmon')
)

STATUS_CHOICES =(
    ('draft', 'DRAFT'),
    ('published', 'PUBLISHED'),
    ('removed', 'REMOVED')
)
class Category(models.Model):
    name= models.CharField(max_length=50, unique=True)
    description= models.TextField()
    slug= models.SlugField(null=False, blank=False, unique=True)
    color= models.CharField(max_length=20, choices= COLOR_CHOICES, default='celeste')

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug =slugify(self.name)
        super(Category, self).save(*args,*kwargs)

class Post(models.Model):
    title= models.CharField(max_length=100, null=False)
    content= models.TextField(null=False)
    created_at= models.DateField(auto_now_add=True)
    update_at= models.DateField(auto_now_add=True)
    categories= models.ManyToManyField(Category, through='PostCategory')
    status= models.CharField(choices=STATUS_CHOICES, default='DRAFT', max_length= 10)
    slug= models.SlugField(null=False, blank=False, unique=True)
    image= models.ImageField(upload_to="image", null=True, blank=True)
    reporter= models.ForeignKey(UserModel, on_delete= models.CASCADE )

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug =slugify(self.title)
        super(Post, self).save(*args,*kwargs)    
    
class PostCategory(models.Model):
    post= models.ForeignKey(Post, on_delete= models.CASCADE)
    category= models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('post', 'category')

    def __str__(self):
        return self.post.title + " - "+ self.category.name


class Comment(models.Model):
    author= models.CharField(max_length=30, null = False)
    content= models.TextField(null=False)
    created_at= models.DateField(auto_now_add=True)
    update_at= models.DateField(auto_now_add=True)
    comment_post= models.ForeignKey(Post, on_delete= models.CASCADE)

    def __str__(self):
        return self.author+" - "+self.comment_post.title