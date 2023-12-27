from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static
from .views import posts_by_category, detalle, create_post

urlpatterns = [
    
    path('', views.inicio,name="Inicio"),
    path('posts', views.posts,name="Post"),
   # path('navbar', views.navbar,name="Navbar"),
    path("category/<slug:slug>/", posts_by_category, name="category"),
    path("posts/<slug:slug>/", detalle, name="detail" ),
    path("create", views.create_post, name="create" ),



]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)