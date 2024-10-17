from django.shortcuts import render
from .models import Post

# Create your views here.

def blog(request):
    return render(request, 'blogsection/bloggerpage.html')


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # Retrieve all posts and order them by creation date (newest first)
    return render(request, 'blogsection/bloggerpage.html', {'posts': posts})
