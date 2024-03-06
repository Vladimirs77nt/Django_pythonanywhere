from django.core.management.base import BaseCommand
from online_store.models import Product

class Command(BaseCommand):
    help = "Delete all products"

    def handle(self, *args, **kwargs):
        count = 0
        products = Product.objects.all()
        if products:
            for product in products:
                self.stdout.write(f'Product {product.name} [id:{product.pk}] is delete')
                product.delete()
                count += 1
            self.stdout.write(f'Total: {count} products deleted')
        else:
            self.stdout.write('Products record is empty...')