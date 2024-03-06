from django.contrib import admin
from .models import Client, Product, Order

# СПОСОБ 2 - на семинаре
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):

    # отображаемые поля
    list_display = ['id', 'name', 'date_reg']

    # поля для фильтра
    list_filter = ['name', 'date_reg']

    # поля для сортировки
    list_sort = ['id', 'name', 'date_reg']

    # расширенное управления макетом страницы администрирования
    fieldsets = [('Общие данные:',
                    {'classes': ['wide'],
                     'fields': ['name', 'telephone', 'date_reg'],
                    },
                ),
                ('Подробности:',
                    {'classes': ['collapse'],
                     'description': 'Полная информация',
                     'fields': ['email', 'address'],
                    },
                ),
            ]
    
    # не изменяемые поля
    readonly_fields = ['date_reg']

    # поля для ссылок на редактирование
    list_display_links = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_filter = ['price', 'date_add']
    list_sort = ['id', 'name', 'price', 'date_add']
    fieldsets = [('Общие данные:',
                    {'classes': ['wide'],
                     'fields': ['name', 'price', 'date_add'],
                    },
                ),
                ('Подробности:',
                    {'classes': ['collapse'],
                     'description': 'Полная информация',
                     'fields': ['description', 'quantity', 'image'],
                    },
                ),
            ]
    readonly_fields = ['date_add']
    list_display_links = ['name']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'total_price']
    list_filter = ['client', 'products']
    list_sort = ['id', 'client', 'total_price', 'date_ordered']
    fieldsets = [('Общие данные:',
                    {'classes': ['wide'],
                     'fields': ['client', 'total_price'],
                    },
                ),
                ('Подробности:',
                    {'classes': ['collapse'],
                     'description': 'Полная информация',
                     'fields': ['products', 'date_ordered'],
                    },
                ),
            ]
    readonly_fields = ['date_ordered']
    list_display_links = ['client']