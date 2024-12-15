from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
# Create your views here.

def blog(request):
    posts = Post.objects.all()
    return render(request, 'blogsection/bloggerpage.html', {'posts': posts})

def blog_view(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'blogsection/blog_view.html', {'post': post})

def create_post(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('blog/')
    return render(request, 'blogsection/post_form.html', {'form': form})