from datetime import datetime
from .models import Reminder
import requests
import time

def check_and_notify():
    print("Thread started")
    while True:
        now = datetime.now()
        reminders = Reminder.objects.all()  # Truy vấn sau khi ứng dụng đã sẵn sàng
        for reminder in reminders:
            event_datetime = datetime.combine(reminder.date, reminder.time)
            if now >= event_datetime and (now - event_datetime).total_seconds() < 60:
                message = f"Nhắc nhở: {reminder.reminder} vào {reminder.date} lúc {reminder.time}"
                print(f"Gửi thông báo: {message}")

                requests.post('https://api.mynotifier.app', {
                    'apiKey': '91c1f113-c6a5-4cc8-b3f5-a2c013503c39',
                    'message': message,
                    'type': 'success'
                })

        time.sleep(20)  # Lặp lại mỗi phút
