from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    path('', views.base),
    path('events/', views.events, name='events'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('base/', views.base, name='base'),
    path('save_reminder/', views.save_reminder, name='save_reminder'),
    path('get_reminders/', views.get_reminders, name='get_reminders'),
    path('delete_reminder/<int:id>/', views.delete_reminder, name='delete_reminder'),
    path('logout/', views.logoutPage, name='logout'),
    path('delete_all_reminders/', views.delete_all_reminders, name='delete_all_reminders'),
    path('important/', views.important, name = 'important'),
]