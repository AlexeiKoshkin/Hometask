# Generated by Django 2.2 on 2019-05-01 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20190501_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/img', verbose_name='Обложка'),
        ),
    ]
