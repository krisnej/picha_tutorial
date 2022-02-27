# Picha - Tutorial on Asynchronous Tasks With Django and Celery

Simple Django App That Gets Photos from Flickr Public Feeds

[RealPython.com Tutorial](https://realpython.com/asynchronous-tasks-with-django-and-celery/) 

I adapted the tutorial to work with Django 3.1 and Celery 5.2


## Running locally
Install requirements:
```commandline
pip install -r requirements.txt
```

Start server for django app:
```commandline
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Start redis db:
```commandline
redis-server
```

Start the celery worker:
```commandline
celery -A picha worker -l info
```

Start the celery beat service to run periodically scheduled task:
```commandline
celery -A picha beat -l info
```
