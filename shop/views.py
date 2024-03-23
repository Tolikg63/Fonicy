from django.shortcuts import render
from django.http import HttpRequest
from .models import Service

def index(request: HttpRequest):
    return render(request, 'shop/index.html')


def services(request: HttpRequest):
    context = {
        'services': Service.objects.all()
    }
    return render(request, 'shop/service.html', context=context)


def about(request: HttpRequest):
    return render(request, 'shop/about.html')


def projects(request: HttpRequest):
    return render(request, 'shop/project.html')