# Generated by Django 5.0.1 on 2024-01-02 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twoapp', '0006_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='orders', to='twoapp.product'),
        ),
    ]
