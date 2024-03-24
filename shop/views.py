from django.shortcuts import render
from django.http import HttpRequest
from .models import Service, Project, Testimonial

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
    context = {
        'projects': Project.objects.all()
    }
    return render(request, 'shop/project.html', context=context)


def testimonial(request: HttpRequest):
    context = {
        'testimonials': Testimonial.objects.all()
    }
    return render(request, 'shop/testimonial.html', context=context)


def contacts(request: HttpRequest):
    return render(request, 'shop/contacts.html')