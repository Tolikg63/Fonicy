from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)