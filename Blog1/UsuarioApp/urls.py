# en nombre_de_la_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="Register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
]