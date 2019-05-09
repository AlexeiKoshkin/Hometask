from django.db import models


class Author(models.Model):
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Serie(models.Model):
    name = models.CharField('Название', max_length=30)
    description = models.TextField('Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'


class Genre(models.Model):
    name = models.CharField('Название', max_length=30)
    description = models.TextField('Описание', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Publisher(models.Model):
    name = models.CharField('Название', max_length=30)
    description = models.TextField('Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'
