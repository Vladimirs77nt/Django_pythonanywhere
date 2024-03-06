from django.core.management.base import BaseCommand
from online_store.models import Client, Order

class Command(BaseCommand):
    help = "Get all order by client id."
    
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
    
    def handle(self, *args, **kwargs):
        count = 0
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        text_out = f"All orders for client id:{pk},\n{client}:\n"
        orders = Order.objects.filter(client__pk=pk)
        if orders:
            for order in orders:
                text_out += f'Order [id: {order.pk}]: date ordered: {order.date_ordered}:\n'
                products_in_order = order.products.all()
                for i_product in products_in_order:
                    text_out += f" > {i_product.name}, price: {i_product.price}\n"
                text_out += f' total price: {order.total_price}\n'
                count += 1
            text_out += f'Total: {count} orders\n'
            self.stdout.write(text_out)
        else:
            self.stdout.write(f'Orders record for client id: {pk} - is empty...')