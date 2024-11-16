
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Diary(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    diary = models.TextField()
    def __str__(self):
        return f"{self.date}: {self.diary}"
    
    
class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField(default=timezone.now)
    reminder = models.CharField(max_length=200)
    time = models.TimeField()
    important = models.BooleanField(default=False) 
    repeat = models.CharField(
        max_length=20,
        choices=[('once', 'Once'), ('daily', 'Daily'), ('weekly', 'Weekly'),
                 ('monthly', 'Monthly'), ('yearly', 'Yearly')],
        default='once'
    )

    def __str__(self):
        return f"{self.date}: {self.reminder} : {self.time}"


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        