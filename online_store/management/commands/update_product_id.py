from django.core.management.base import BaseCommand
from online_store.models import Product

class Command(BaseCommand):
    help = "Update product name and prict by id."
    
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('name', type=str, help='Product name')
        parser.add_argument('price', type=int, help='Product price')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        price = kwargs.get('price')
        product = Product.objects.filter(pk=pk).first()
        product.name = name
        product.price = price
        product.save()
        self.stdout.write(f'{product}')