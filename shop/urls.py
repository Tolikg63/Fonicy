from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('testimonials/', views.testimonial, name='testimonial'),
    path('contacts/', views.contacts, name='contacts'),
]