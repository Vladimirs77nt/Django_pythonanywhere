from django.core.management.base import BaseCommand
from online_store.models import Product

class Command(BaseCommand):
    help = "Get all products."
    
    def handle(self, *args, **kwargs):
        count = 0
        products = Product.objects.all()
        if products:
            for product in products:
                self.stdout.write(f'Product [id: {product.pk}]: {product}')
                count += 1
            self.stdout.write(f'Total: {count} products')
        else:
            self.stdout.write('Products record is empty...')