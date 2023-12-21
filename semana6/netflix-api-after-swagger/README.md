## Installing and running a Django project

```
pip install django
django-admin startproject netflix_api .
python manage.py runserver
```

### Creating a superuser

```
python manage.py migrate
python manage.py createsuperuser
```

### Migrate

```
python manage.py makemigrations subscription
python manage.py migrate subscription
```

### To start a new app

```
python manage.py startapp product
Then modify INSTALLED_APPS. Add product
```

### Terminal shell de django

```
python manage.py shell
```

```
>>> from subscription.models import Subscription
>>> new_register = Subscription(title="Basico", description="1 tv",price=24.9)
>>> new_register.save()
```

### Django

```
Django es un Monolito = Frontend (templates)/Backend = Todo en uno <-- safer
DRF = Django Rest Framework
Django + DRF => API
```

### DRF

```
pip install djangorestframework
from rest_framework.viewsets import ModelViewSet
serializers.py en cada app
```

### Swagger

```
pip install drf-yasg
http://127.0.0.1:8000/swagger/
```

### JWT

```
pip install djangorestframework-simplejwt
```

### Requests

```
pip install requests

```
