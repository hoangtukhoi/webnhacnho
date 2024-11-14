from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from .models import *
import json
from datetime import timedelta
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import calendar
from datetime import datetime
from .models import Reminder
from .forms import ReminderForm
from threading import Thread
from .notify import check_and_notify
from django.http import JsonResponse
from .models import Reminder  # Giả sử bạn đã có model Reminder

def home(request):
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
# Tạo trang 
def register(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid:
            form.save()
    context = {'form': form}
    return render(request,'app/register.html', context  )
def loginPage(request):
    
    if request.user.is_authenticated :
        return redirect('home')
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
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            reminder_text = form.cleaned_data['reminder']
            reminder_time = form.cleaned_data['time']
            Reminder.objects.create(
                user=request.user,  # Gán user hiện tại vào reminder
                date=date,
                reminder=reminder_text,
                time=reminder_time
            )
            return redirect('events')

    # Hiển thị form và tất cả các reminders
    form = ReminderForm(initial={'date': timezone.now().date()})
    reminders = Reminder.objects.filter(user=request.user).order_by("date", "time")
    return render(request, 'app/events.html', {'form': form, 'reminders': reminders})
def home(request):
    return render(request, 'app/home.html')

def save_reminder(request):
    if request.method == 'POST':
        reminder_text = request.POST.get('reminder')
        reminder_date = request.POST.get('date')
        reminder_time = request.POST.get('time')
        reminder_repeat = request.POST.get('repeat')
        # Chuyển đổi chuỗi thành đối tượng ngày tháng
        from datetime import datetime
        reminder_date = datetime.strptime(reminder_date, '%d-%m-%Y')
        
        # Tạo reminder mới và lưu vào DB
        Reminder.objects.create(
            user = request.user,
            reminder=reminder_text,
            date=reminder_date,
            time=reminder_time,
            repeat=reminder_repeat
        )
        if reminder_repeat == "daily":
            for i in range(1, 30):  # Lặp lại 3 tuần nữa (4 lần tổng cộng)
                repeat_date = reminder_date + timedelta(days=i)
                Reminder.objects.create(
                    user = request.user,
                    reminder=reminder_text,
                    date=repeat_date,
                    time=reminder_time,
                    repeat=reminder_repeat
                )
        if reminder_repeat == "weekly":
            for i in range(1, 12):  # Lặp lại 3 tuần nữa (4 lần tổng cộng)
                repeat_date = reminder_date + timedelta(weeks=i)
                Reminder.objects.create(
                    user = request.user,
                    reminder=reminder_text,
                    date=repeat_date,
                    time=reminder_time,
                    repeat=reminder_repeat
                )
        
        return JsonResponse({'message': 'Reminder saved successfully!'})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
    # views.py
from django.http import JsonResponse

def get_reminders(request):
    reminders = Reminder.objects.filter(user=request.user)
    reminders_data = [
        {
            'eventName': reminder.reminder,
            'eventTime': reminder.time,
            'calendar': 'Default',
            'color': 'orange',  # Default color
            'date': reminder.date.strftime('%Y-%m-%d')  
        }
        for reminder in reminders
    ]
    return JsonResponse(reminders_data, safe=False)
def delete_reminder(request, id):
    if request.method == 'POST':
        try:
            reminder = Reminder.objects.get(id=id)
            reminder.delete()
            return JsonResponse({'status': 'success'})
        except Reminder.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Event not found'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})
def logoutPage(request):
    logout(request)
    return redirect('login')

if __name__ == "__main__":
    t = Thread(target=check_and_notify)
    t.daemon = True  
    t.start()
    

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def delete_all_reminders(request):
    if request.method == 'POST':
        # Xóa tất cả các sự kiện
        Reminder.objects.filter(user=request.user).delete()
        return JsonResponse({'message': 'All reminders have been deleted.'})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)