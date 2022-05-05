from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index1, name='index1'),
    path('cities/', views.city, name='city'),
    path('universities/', views.university, name='university'),
    path('foods/', views.foods, name='foods'),
    path('feedback/', views.feedback, name='feedbacks'),
    path('feedback/upload/', views.upload, name='upload-book'),
    path('feedback/update/<int:book_id>', views.update_book),
    path('feedback/delete/<int:book_id>', views.delete_book),
    path('women/<slug:women_slug>', views.women_slug, name='women_slug'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('contact/', EmailView.as_view(), name='contact'),
]