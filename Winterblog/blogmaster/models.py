from django.db import models

# blog/models.py

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')  # Add the image field

    def __str__(self):
        return self.title


# Create your models here.

# MD Imdadul Hossain Info

class My_info(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField()
    Degree = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class My_education(models.Model):
    name = models.CharField(max_length=50)
    institute = models.CharField(max_length=50)
    year = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class My_experience(models.Model):
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    desc = models.TextField()

    def __str__(self):
        return self.name

class My_service(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    icon_type = models.CharField(max_length=50)
    desc = models.TextField()

    def __str__(self):
        return self.name