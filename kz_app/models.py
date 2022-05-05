from django.db import models
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class University(models.Model):
    university_name = models.CharField(max_length=50)
    location = models.CharField(max_length=250)
    year = models.IntegerField()
    description = models.TextField()
    class Meta:
        verbose_name = 'University'
        verbose_name_plural = 'Universities'

class Cities(models.Model):
    city_name = models.CharField(max_length=50)
    description = models.TextField()
    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
    def __str__(self):
        return self.city_name

class Food(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    images = models.ImageField()
    class Meta:
        verbose_name = 'Food',
        verbose_name_plural = 'Foods'

class Feedback(models.Model):
    name = models.CharField(max_length = 50)
    author = models.CharField(max_length = 30, default='anonymous')
    feedback = models.TextField(default = 'That was amazing!!!')
    class Meta:
        verbose_name = 'Feedback',
        verbose_name_plural = 'Feedbacks'
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('feedback-detail', args=[str(self.id)])

class Womens_of_Kazakhstan(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    link = models.CharField(max_length=250, null=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL', null=True)
    class Meta:
        verbose_name = 'Women_of_Kazakhstan',
        verbose_name_plural = 'Womens_of_Kazakhstan'
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('category', kwargs={'women_slug': self.slug})



