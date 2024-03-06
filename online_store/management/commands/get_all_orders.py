from django.core.management.base import BaseCommand
from online_store.models import Client, Product, Order

class Command(BaseCommand):
    help = "Get all orders."
    
    def handle(self, *args, **kwargs):
        count = 0
        clients = Client.objects.all()
        products = Product.objects.all()
        
        orders = Order.objects.all()
        if orders:
            for order in orders:
                products_in_order = order.products.all()
                print(f'Order [id: {order.pk}]: {order.client.name}, date ordered: {order.date_ordered}:')
                for i_product in products_in_order:
                    print (f" > {i_product.name}, price: {i_product.price}")
                print(f' total price: {order.total_price}:')
                count += 1
            self.stdout.write(f'Total: {count} orders')
        else:
            self.stdout.write('Orders record is empty...')