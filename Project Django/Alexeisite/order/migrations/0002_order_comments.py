# Generated by Django 2.2 on 2019-05-20 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='comments',
            field=models.TextField(blank=True, null=True, verbose_name='Дополнительная информация'),
        ),
    ]