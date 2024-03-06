from datetime import date
import random
from django.core.management.base import BaseCommand
from online_store.models import Product
import faker    # генерация фейковых имен и фамилий

fake = faker.Faker('ru_RU')

class Command(BaseCommand):
    help = "Create Products (random)"

    def handle(self, *args, **kwargs):
        count = 100  # количество создаваемых товаров
        for i in range(count):
            product = Product(name=f'Item_0000-{random.randint(1,1000)}',
                              description=fake.paragraph(nb_sentences=5),
                              price = random.randint(1,1000),
                              quantity = random.randint(1,100),
                              date_add = date(year=random.randint(2018,2022), month=random.randint(1,12), day=random.randint(1,30)))
            product.save()
            id_latest = Product.objects.latest('pk')
            print (f'{id_latest=}')
            product.name = f'Item_{id_latest.pk}-{random.randint(1,1000)}'
            product.save()
            self.stdout.write(f'Create product [id:{product.pk}]: {product}')
        self.stdout.write(f'Total: {count} products create')