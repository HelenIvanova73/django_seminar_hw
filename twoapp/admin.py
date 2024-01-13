from django.contrib import admin
from django.utils.html import mark_safe
from twoapp.models import Client, Product, Order


# Register your models here.
class OrderInline(admin.TabularInline):
    model = Order
    extra = 0

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'address')
    list_display_links = ('name', 'phone_number')
    inlines = [OrderInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'qwontity', 'display_image')
    list_display_links = ('name', 'description')

    def display_image(self, obj):
        # Здесь вы можете создать HTML-код для отображения изображения
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        else:
            return 'Нет изображения'

    display_image.short_description = 'Изображение'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'total_price')
    list_display_links = ('client',)
    fields = ('client', 'total_price')
    readonly_fields = ('total_price',)

