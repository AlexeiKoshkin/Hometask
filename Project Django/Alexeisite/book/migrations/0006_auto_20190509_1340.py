# Generated by Django 2.2 on 2019-05-09 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20190501_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Обложка'),
        ),
    ]
