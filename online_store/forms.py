from django import forms
from .models import Product


class ProductForm (forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = Product
        exclude = ['date_add']
        labels = {'name': 'Название товара',
                  'description': 'Описание',
                  'price': 'Цена',
                  'quantity': 'Количество в наличии',
                  'image': 'Изображение'}