# Generated by Django 2.2 on 2019-06-04 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20190604_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_cart', to='cart.Cart', verbose_name='Корзина'),
        ),
    ]
