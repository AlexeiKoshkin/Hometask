# Generated by Django 2.2 on 2019-05-09 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0004_remove_genre_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]
