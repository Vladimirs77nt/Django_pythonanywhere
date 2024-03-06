from datetime import datetime, timedelta
from random import randint, choice
from django.core.management.base import BaseCommand
from online_store.models import Client, Product, Order
from django.utils import lorem_ipsum

class Command(BaseCommand):
    help = "Create Orders (random)"

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        products = Product.objects.all()

        for client in clients:
            time_delta = timedelta(days=randint(0,10))
            time_order = datetime.now() - time_delta
            order = Order(client=client,
                          total_price=0,
                          date_ordered=time_order)
            order.save()
            total_price = 0
            for i in range(randint(1,6)):   # от 1 до 5 товаров в заказе
                product = choice(products)
                order.products.add(product)
                order.save()
                total_price += product.price
            order.total_price = total_price
            order.save()
            print (order)

        self.stdout.write(f'All orders - created')