from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from .models import *
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import calendar
from datetime import datetime

def home(request):
    print("View home đã được gọi")  # Thêm dòng này để kiểm tra
    now = datetime.now()
    month = now.month
    year = now.year
    month_calendar = calendar.monthcalendar(year, month)

    context = {
        'month_calendar': month_calendar,
        'month': calendar.month_name[month],
        'year': year,
    }
    return render(request, 'app/home.html', context)
# Create your views here.
def register(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid:
            form.save()
    context = {'form': form}
    return render(request,'app/register.html', context  )
def loginPage(request):
    
    # if request.user.is_authenticated :
    #     return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username hoặc password chưa đúng!')
    context = {}
    return render(request,'app/login.html', context  )
def base(request):
    return render(request, 'app/base.html')
def events(request):
    return render(request, 'app/events.html')
def home(request):
    return render(request, 'app/home.html')
def lich(request):
    return render(request, 'app/lich.html')
from .models import Reminder
from .forms import ReminderForm
def datepicker_example(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            reminder_text = form.cleaned_data['reminder']
            Reminder.objects.create(date=date, reminder=reminder_text)  # Lưu nhắc nhở vào cơ sở dữ liệu
            return redirect('datepicker_example')

    form = ReminderForm(initial={'date': timezone.now().date()})
    reminders = Reminder.objects.all()  # Lấy tất cả nhắc nhở từ cơ sở dữ liệu

    return render(request, 'app/lich.html', {'form': form, 'reminders': reminders})
