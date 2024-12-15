from django.shortcuts import render
from .models import Post, My_info, My_education, My_experience, My_service


# Create your views here.

def home(request):
    posts = Post.objects.all()
    my_info = My_info.objects.all()
    my_education = My_education.objects.all()
    my_experience = My_experience.objects.all()
    my_service = My_service.objects.all()
    # Render the posts to the template
    return render(request,
     'blogmaster/home.html',
           {'posts': posts,
                   'my_info':my_info,
                   'my_education':my_education,
                   'my_experience':my_experience,
                   'my_service':my_service })
