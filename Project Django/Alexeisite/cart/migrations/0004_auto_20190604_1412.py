# Generated by Django 2.2 on 2019-06-04 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20190604_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookincart',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book', verbose_name='Книга'),
        ),
    ]