import datetime
import random

from django.db import models
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class Food(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    images = models.ImageField(upload_to='static/kz_app/img', default=True)
    class Meta:
        verbose_name = 'Food',
        verbose_name_plural = 'Foods'
    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length = 50)
    author = models.CharField(max_length = 30)
    feedback = models.TextField(default = 'That was amazing!!!')
    class Meta:
        verbose_name = 'Feedback',
        verbose_name_plural = 'Feedbacks'
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('feedback-detail', args=[str(self.id)])

class Sportmasters_of_Kazakhstan(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    link = models.CharField(max_length=250, null=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL', null=True)
    class Meta:
        verbose_name = 'Sportmasters_of_Kazakhstan',
        verbose_name_plural = 'Sportmasters_of_Kazakhstan'
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('category', kwargs={'master_slug': self.slug})

def random_num():
    return str(random.randint(10000000, 99999999))

class City(models.Model):
    name = models.CharField(max_length=100, default=True)
    description = models.TextField()
    image = models.ImageField(upload_to='static/kz_app/img', default='default.jpg')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL', null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Cities'
    def get_absolute_url(self):
        return reverse('city', kwargs={'city_slug': self.slug})


