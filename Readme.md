Windows:
https://www.codingforentrepreneurs.com/blog/install-python-django-on-windows/
Install pip
`python -m pip install pipenv`

Create virtual environment
`python -m venv venv`

install requirements
`pipenv install`

run env
`source venv/Scripts/activate`
or
`pipenv run activate`
or
`pipenv shell`

Create a django project
`django-admin startproject <mysite>`

Cd to `<mysite>` and run `python manage.py runserver 8000` to start the server

Postgres
- install postgres
- `pip3 install psycopg2`
- add db connection info
```python
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

To create a superuser on said db
`python manage.py createsuperuser`

chris
boomroot

Create a new folder to house individual apps.
`python manage.py startapp <app_name>`


Adding rest_framework
`'rest_framework'` to installed apps in settings

Add auth and permissions to settings file

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
}
```

Running client
`python py_client/basic.py`

Running the python backend
`python backend/manage.py runserver 8000`

creating new apps
`python manage.py startapp appName`

Migrate new model changes
`python backend/manage.py makemigrations`
`python backend/manage.py migrate`