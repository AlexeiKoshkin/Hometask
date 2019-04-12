from reference.models import *
from book.models import *

# 2


def create_serie(data):
    # data={'name': Имя серии, 'description': Описание}
    ser = Serie(
        name=data['name'],
        description=data['description']
        )
    ser.save()
    print('The object with pk = {} was created'.format(ser.pk))


def create_author(data):
    aut = Author(
        first_name=data['first_name'],
        last_name=data['last_name']
        )
    aut.save()
    print('The object with pk = {} was created'.format(aut.pk))


def create_genre(data):
    gen = Genre(
        name=data['name'],
        )
    gen.save()
    print('The object with pk = {} was created'.format(gen.pk))


def create_publisher(data):
    pub = Publisher(
        name=data['name'],
        description=data['description']
        )
    pub.save()
    print('The object with pk = {} was created'.format(pub.pk))

# 3


def delete_object(data):
    # data={'Название справочника': Author, 'Primary Key элемента': 10}
    b = data['ref'].objects.get(
        pk=data['pk']
        )
    b.delete()
    print('The object with was deleted')

# 4


def num_author():
    n = Author.objects.all()
    print(len(n))

# 5


def random_author():
    for i in range(1, 10):
        aut = Author(
            first_name='name' + str(i),
            last_name='last_name' + str(i)
            )
        aut.save()
        print('The object with pk = {} was created'.format(aut.pk))

# 6


def num_name_author(data):
    n = Author.objects.filter(first_name__startswith=data)
    print(len(n))


# 7

def create_book(data):
    obj = Book(
        name=data['name'],
        price=data['price'],
        issue_year=data['issue_year'],
        page=data['page'],
        binding=data['binding'],
        size=data['size'],
        isbn=data['isbn'],
        weight=data['weight'],
        age_rest=data['age_rest'],
        num_book=data['num_book'],
        available=data['available'],
        rating=data['rating'])
    obj.serie = Serie.objects.get(pk=data['serie_name'])
    obj.genre = Genre.objects.get(pk=data['genre_name'])
    obj.publisher = Publisher.objects.get(pk=data['publisher_name'])
    obj.save()
    aut = Author.objects.get(pk=data['first_name'])
    obj.authors.add(aut)


data = {'name': 'Книга', 'price': 200, 'issue_year': 2001, 'page': 658, 'binding': 'Твердый переплет' ,
'size': '84х108/32 (130х205 мм, стандартный)', 'isbn': '978-5-699-34667-7', 'weight': 555, 'age_rest': '18+', 'num_book': 2, 'available': True, 'rating': 5, 'first_name': 21, 'serie_name': 14, 'genre_name': 4, 'publisher_name': 2}


# 8


def update_create(data):
    obj, created = Author.objects.update_or_create(
        first_name=data['first_name'],
        defaults={'last_name': data['last_name']}
        )


# 9


def list_author(data):
    n = Author.objects.get(first_name=data)
    k = n.Book.all()
    print(k)
