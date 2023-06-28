## Steps

    python -m django --version
    pip install django
    
    django-admin startproject mysite
    python manage.py startapp bibliography
    
    python manage.py migrate
    python manage.py runserver
    
    python manage.py makemigrations bibliography
    python manage.py sqlmigrate bibliography 0001
    python manage.py migrate

    python manage.py shell
    from bibliography.models import *

## Admin App

    python manage.py createsuperuser

## Shell

    BibTag.objects.all()
    from django.utils import timezone
