from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.blog, name='home'),
    path('posts/', views.post_list, name='post_list'),
]