from django.apps import AppConfig
import threading

def start_notification_thread():
    from app.notify import check_and_notify
    notification_thread = threading.Thread(target=check_and_notify)
    notification_thread.daemon = True
    notification_thread.start()

class AppConfig(AppConfig):
    name = 'app'

    def ready(self):
        start_notification_thread()