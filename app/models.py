
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib.auth.models import User

class Reminder(models.Model):
    date = models.DateField()
    reminder = models.CharField(max_length=200)
    time = models.TimeField()
    def __str__(self):
        return f"{self.date}: {self.reminder}:{self.time}"

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        