# Library

> The project is a basic `API` based project. The following steps will walk you thru installation on a Mac. Linux should be similar. It's also possible to develop on a Windows machine, but I have not documented the steps. If you've developed django apps on Windows, you should have little problem getting up and running.

### Setup
- Python 3.8
- Django 3.1.4
- postgres

###### Dependancies
Install `postgres` database in the django app
```base
pip install django gunicorn psycopg2
```

Install Django default restful api (DRF). 1st install virtualenv in your project then follow the command line.
```
source venv/bin/activate
pip install djangorestframework
```
###### Configuration database in the project. Open settings.py then follow the instraction

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'libary',
        'USER': 'sagor',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```
