#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.management import execute_from_command_line
from django.core.management import call_command

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webnhacnho.settings')
    
    # Chạy custom command khi server khởi động
    # if 'runserver' in sys.argv:
    #     call_command('run_notify')

    # Thực thi các câu lệnh Django
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
