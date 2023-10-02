import os
from django.core.management import execute_from_command_line
from django.conf import settings
import env

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tundorul_django.settings')

if __name__ == '__main__':
    args = ['manage.py', 'runserver']
    execute_from_command_line(args)
