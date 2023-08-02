from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.author} - {self.title}'