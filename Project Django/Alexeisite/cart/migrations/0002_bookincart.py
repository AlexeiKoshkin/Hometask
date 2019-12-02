# Generated by Django 2.2 on 2019-05-13 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_auto_20190509_1340'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookInCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания корзины')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books_in_cart', to='cart.Cart', verbose_name='Книга в корзине')),
            ],
            options={
                'verbose_name': 'Книга в корзине',
                'verbose_name_plural': 'Книги в корзине',
                'unique_together': {('cart', 'book')},
            },
        ),
    ]