from django.core.management import BaseCommand
from shop.models import Service


class Command(BaseCommand):
    def handle(self, *args, **options):
        service_names = [
            ("CONSTRUCTION SERVICES", "fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using L", 80000),
            ("BUILDING MODELING", "fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using L", 75000),
            ("PRE CONSTRUCTION", "fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using L", 90000),
            ("MANAGEMENT", "fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using L", 100000)
        ]

        for service_name, description, price in service_names:
            service = Service.objects.get_or_create(name=service_name, description=description, price=price)
