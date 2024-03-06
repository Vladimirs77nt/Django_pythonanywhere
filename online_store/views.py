import datetime
import logging

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.files.storage import FileSystemStorage

from .forms import ProductForm
from .models import Client, Product, Order


logger = logging.getLogger(__name__)

def store_index(request):
    text = 'Index page "Online Store Start" accessed'
    logger.info(text)   
    return render(request, 'online_store/store_index.html', {'text': text})

def clients_all(request):
    clients = Client.objects.all()
    logger.info('Index page "Client ALL" accessed')
    return render(request, 'online_store/clients_all.html', {'clients': clients})

def client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client__pk=client_id)
    logger.info('Index page "Client" accessed')
    return render(request, 'online_store/client.html', {'client': client, 'orders': orders})

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    image_old = product.image

    logger.info('Index page "Product" accessed')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            print ('валидация пройдена')
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            image = form.cleaned_data['image']

            if image:
                print (f"изображение: загружено новое изображение {image}")
                product = Product (pk = product_id,
                                    name = name,
                                    description = description,
                                    price = price,
                                    quantity = quantity,
                                    image = image)
                fs = FileSystemStorage()    # загруженное изображение
                print ('fs =', fs)
                fs.save(image, image)  # сохранение в папку 'media'
            else:
                print ("изображение: НОВОЕ ИЗОБРАЖЕНИЕ НЕ ЗАГРУЖЕНО !")
                product = Product (pk = product_id,
                                    name = name,
                                    description = description,
                                    price = price,
                                    quantity = quantity,
                                    image = image_old)
            product.save()
            return redirect('product', product_id)
        else:
            print ('валидация НЕ пройдена !!!')
    else:
        form = ProductForm(instance=product)

    return render(request, 'online_store/product.html', {'product': product, 'form':form})

def products_all(request):
    products = Product.objects.all()
    logger.info('Index page "Products ALL" accessed')
    return render(request, 'online_store/products_all.html', {'products': products})

def order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    products_in_order = order.products.all()
    return render(request, 'online_store/order.html', {'order': order, 'products_in_order': products_in_order})


"""
Задание №7 (с семинара)
    Доработаем задачу 8 из прошлого семинара про клиентов, товары и заказы.
    Создайте шаблон для вывода всех заказов клиента и списком товаров внутри каждого заказа.
    Подготовьте необходимый маршрут и представление.
"""
def orders_by_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client__pk=client_id)
    return render(request, 'online_store/orders_no_sort.html', {'orders': orders, 'client': client})


"""
Домашнее задание:
    Продолжаем работать с товарами и заказами.
    Создайте шаблон, который выводит список заказанных клиентом товаров
    из всех его заказов с сортировкой по времени:
        * за последние 7 дней (неделю)
        * за последние 30 дней (месяц)
        * за последние 365 дней (год)
    * Товары в списке не должны повторятся.
"""
def orders_by_client_sort(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client__pk=client_id).order_by('-date_ordered')
    orders_7 = []
    orders_30 = []
    orders_365 = []
    for order in orders:
        date_delta = datetime.date.today() - order.date_ordered
        date_delta = int (date_delta.days)
        print (date_delta)
        if date_delta <= 365:
            orders_365.append(order)
            if date_delta <= 30:
                orders_30.append(order)
                if date_delta <= 7:
                    orders_7.append(order)

    return render(request, 'online_store/orders_sort.html', {'orders_7': orders_7,
                                                             'orders_30': orders_30,
                                                             'orders_365': orders_365,
                                                             'client': client})