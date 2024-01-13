from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    date_registration = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    qwontity = models.IntegerField()
    date_registration = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    products = models.ManyToManyField(Product, related_name='orders')
    date_registration = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Переместите этот импорт вверх, если он еще не произошел
        from django.db.models import Sum

        # Обновим total_price только если объект Order уже имеет первичный ключ
        if self.pk:
            products_total_price = self.products.aggregate(Sum('price'))['price__sum']
            self.total_price = products_total_price if products_total_price else 0

        super().save(*args, **kwargs)


    def __str__(self):
        return str(self.id)