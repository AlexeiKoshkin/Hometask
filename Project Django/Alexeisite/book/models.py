from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(
        "Название книги",
        null=True,
        blank=True,
        max_length=200
    )
#   image = models.ImageField(
#        "Обложка",
#        upload_to=None
#    )
    price = models.DecimalField(
        "Цена",
        max_digits=8,
        decimal_places=2
    )
    authors = models.ManyToManyField(
        "reference.Author"
    )
    serie = models.ForeignKey(
        "reference.Serie",
        verbose_name="Серия",
        on_delete=models.CASCADE,
        related_name="books"
    )
    genre = models.ForeignKey(
        "reference.Genre",
        verbose_name="Жанр",
        on_delete=models.CASCADE,
        related_name="books"
    )
    issue_year = models.IntegerField(
        "Год издания"
    )
    page = models.IntegerField(
        "Страниц"
    )
    binding = models.CharField(
        "Переплет",
        max_length=200
    )
    size = models.CharField(
        "Формат",
        max_length=200
    )
    isbn = models.CharField(
        "ISBN",
        max_length=200
    )
    weight = models.IntegerField(
        "Вес"
    )
    age_rest = models.CharField(
        "Возрастные ораничения",
        max_length=10
    )
    publisher = models.ForeignKey(
        "reference.Publisher",
        on_delete=models.CASCADE,
        related_name="books"
    )
    num_book = models.IntegerField(
        "Количество книг в наличии"
    )
    available = models.BooleanField(
        "Доступна для заказа",
        default=True
    )
    rating = models.FloatField(
        "Рейтинг"
    )
    created_date = models.DateTimeField(
        "Дата создания",
        auto_now=False,
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        "Дата изменения",
        auto_now=True,
        auto_now_add=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
