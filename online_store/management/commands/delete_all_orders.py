from django.core.management.base import BaseCommand
from online_store.models import Client, Product, Order

class Command(BaseCommand):
    help = "Get all orders."
    
    def handle(self, *args, **kwargs):
        count = 0
        orders = Order.objects.all()
        if orders:
            for order in orders:
                self.stdout.write(f'Order [id: {order.pk}]: is delete...')
                order.delete()
                count += 1
            self.stdout.write(f'Total: {count} orders deleted')
        else:
            self.stdout.write('Orders record is empty...')