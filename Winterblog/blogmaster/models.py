from django.db import models

# blog/models.py

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')  # Add the image field

    def __str__(self):
        return self.title


# Create your models here.
