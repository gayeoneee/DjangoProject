from django.contrib import admin
from django.urls import path
from blog import views

ulrpatterns = [
    path("", views.home, name="home"), # 127.0.0.1:8000/home/
    path("create/", views.home, name="home"),  # 127.0.0.1:8000/home/create/
]