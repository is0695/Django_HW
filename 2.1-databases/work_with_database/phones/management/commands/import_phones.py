import csv
from django.utils.text import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            id, name, image, price, release_date, lte_exists =(
                phone['id'], phone['name'], phone['image'], phone['price'],
                phone['release_date'], phone['lte_exists'])
            slug = slugify(phone['name'])
            phone = Phone(id=id, name=name, image=image, price=price, release_date=release_date,
                          lte_exists=lte_exists, slug=slug)
            phone.save()

