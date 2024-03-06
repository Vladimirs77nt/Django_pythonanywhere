"""
Создайте три модели Django: клиент, товар и заказ.
    ○ Клиент может иметь несколько заказов.
    ○ Заказ может содержать несколько товаров.
    ○ Товар может входить в несколько заказов.
"""

from django.db import models

"""
---------------------------------------------------------------------------------
Поля модели «Клиент» (client):
    — имя клиента
    — электронная почта клиента
    — номер телефона клиента
    — адрес клиента
    — дата регистрации клиента
"""
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=32)
    telephone = models.EmailField()
    password = models.CharField(max_length=12)
    address = models.CharField(max_length=32)
    date_reg = models.DateField()

    def __str__(self):
        return f'{self.name}'


"""
---------------------------------------------------------------------------------
Поля модели «Товар» (product):
    — название товара
    — описание товара
    — цена товара
    — количество товара
    — дата добавления товара
"""
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    date_add = models.DateField(auto_now=True)
    image = models.ImageField()

    def __str__(self):
        return f'{self.name}, price: {self.price}, quantity: {self.quantity}'

"""
---------------------------------------------------------------------------------
Поля модели «Заказ» (order):
    — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
    — связь с моделью «Товар», указывает на товары, входящие в заказ
    — общая сумма заказа
    — дата оформления заказа
"""
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateField()

    def __str__(self):
        text_out = f'{self.client.name}, date ordered: {self.date_ordered}:\n'
        products_in_order = self.products.all()
        for i_product in products_in_order:
            text_out += f" > {i_product.name}, price: {i_product.price}\n"
        text_out += f' total_price: {self.total_price}'
        return f'Order [id: {self.pk}] {text_out}'