from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=800)
    date = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField(upload_to='images/')