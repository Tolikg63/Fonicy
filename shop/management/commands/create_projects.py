from typing import Any
from django.core.management import BaseCommand
from shop.models import Project

class Command(BaseCommand):
    def handle(self, *args, **options):
        project_names = [
            ("Interior work", "alteration in some form, by injected, or randomised words which don't look even slightly believable to unbelievable")
        ]


        for project_name, description in project_names:
            Project.objects.get_or_create(name=project_name, description=description)