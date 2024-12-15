from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} to {self.author}"
    # Custom method to return full details as a dictionary
    def get_full_details(self):
        return {
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField(default=0)

    def __str__(self):
        return self.item_name

class List(models.Model):
    def __str__(self):
        return self.list_name
    list_name = models.CharField(max_length=200)
    list_desc = models.CharField(max_length=200)
    list_price = models.IntegerField(default=0)