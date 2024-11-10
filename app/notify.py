import time
from datetime import datetime
import requests
from app.models import Reminder 

def check_and_notify():
    print("Thread started")
    while True:
        now = datetime.now()
        reminders = Reminder.objects.all()  
        for reminder in reminders:
            event_datetime = datetime.combine(reminder.date, reminder.time)
            if now >= event_datetime and (now - event_datetime).total_seconds() < 60:
                message = f"Ngài tổng tài, ngài có việc: {reminder.reminder} vào {reminder.date} lúc {reminder.time}"
                requests.post('https://api.mynotifier.app', {
                    'apiKey': '353b5571-d43e-4890-8234-dbd620a8395f', # thay đổi API để hiện tb về máy
                    'message': message,
                    'type': 'success'
                })

        time.sleep(60)
