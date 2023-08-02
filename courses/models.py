from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class Course(models.Model):
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='courses', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=3)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.title}'

    
class Episode(models.Model):
    course = models.ForeignKey(
        Course, 
        on_delete=models.CASCADE, 
        related_name="episodes"
    )
    title = models.CharField(max_length=255)
    video = models.FileField(
        upload_to="episodes", 
        validators=[
            FileExtensionValidator
            (allowed_extensions=['MOV','avi','mp4','webm','mkv'])]
    )
    
    def __str__(self):
        return f'{self.course.title} - {self.title}'