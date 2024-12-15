from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blogsection'
urlpatterns = [
    # Url for the home route
    path('', views.blog, name='blog'),
    # URl for the blog section
    path('blog/', views.blog, name='post_list'),
    #/blogsection/1
    path('<int:id>/', views.blog_view, name='blog_view'),
    # path('post/<int:id>/', views.detail_view, name='detail_view'),
    # Url for the form that add post
    path('add', views.create_post, name='create_post')
]