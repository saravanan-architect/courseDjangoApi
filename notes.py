"""
virtual environment setup
python3 -m venv venv
source venv/bin/activate

deactivate for deactivating
pip3 freeze for checking installed packages
    asgiref==3.8.1
    backports.zoneinfo==0.2.1
    Django==4.2.16
    djangorestframework==3.15.2
    sqlparse==0.5.1
    typing-extensions==4.12.2

pip3 install django
pip3 install djangorestframework

start project
django-admin startproject djangoapi

add to settings.py, installed_apps
'rest_framework',

linux-migrate:
python3 manage.py migrate

windows-migrate:
winpty python3 manage.py migrate

python3 manage.py runserver

python3 manage.py startapp courses

add courses to installed_apps in  settings.py

create superuser
python3 manage.py createsuperuser

python3 manage.py makemigrations
python3 manage.py migrate

register models in admin.py
add urls.py
"""