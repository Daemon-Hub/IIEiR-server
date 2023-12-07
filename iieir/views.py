from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Сайт ИИЭиР!!!")


def events(requsts):
    return HttpResponse("Обьявления ИИЭиР!!!")


def login(requsts):
    return HttpResponse("Вход в сайт ИИЭиР!!!")


def register(requsts):
    return HttpResponse("Регистрация на сайт ИИЭиР!!!")

