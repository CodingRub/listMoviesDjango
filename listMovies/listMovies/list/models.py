from django.db import models
from django.urls import reverse

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=100)
    synopsis = models.TextField()
    date_released = models.DateField()
    author = models.CharField(max_length=150)
    time = models.CharField(max_length=50)
    genre = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='images/', default='/images/1000x1481.png') 


    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})