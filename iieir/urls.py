from django.urls import path
from .views import (index, events, login, register)


urlpatterns = [
    path('', index, name='index'),
    path('events/', events, name='events'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]
