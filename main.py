from conf import MODEL
import random
from faker import Faker
import json
fake = Faker()
Faker.seed(0)


#Шаблон словаря
def book_init() -> dict:
    Book = {"model": "shop_final.book",
            "pk": 1,
            "fields": {
                "title": "test_book",
                "year": 2020,
                "pages": 123,
                "isbn13": "978-1-60487-647-5",
                "rating": 5,
                "price": 123456.0,
                "author": [
                    "test_author_1",
                    "test_author_2"
                           ]

                       }
            }
    return Book


# Ф-ция возвращает значение ключа 'model' из импортируемого словаря (переменной) MODEL
def get_model() -> dict:
    return MODEL['model']


#Ф-ция создает генератор названия книг, затем рандомно возвращает название одной книги
def get_book() -> str:
    books = (x.strip() for x in list(open('books.txt', 'r', encoding='utf-8')))
    n = random.randrange(1, 6)
    for i in range(n):
        b = next(books)
    return b


# Рандомный год
def get_year() -> int:
    return random.randint(1900, 2022)


# Рандомное кол-во страниц
def get_page() -> int:
    return random.randint(1, 1000000)


#Рандомный рейтинг
def get_rating() -> float:
    return random.uniform(0.0, 5.)


# Рандомная стоимость книги
def get_price() -> float:
    return random.uniform(0, 10000)


# Рандомные isbn из библиотеки Faker
def get_isbn() -> str:
    return fake.isbn13()


# Рандомные авторы (от 1 до 3) из библиотеки Faker
def get_author() -> list:
    author = []
    n = random.randrange(1, 4)
    for i in range(n):
        author.append(fake.name())
    return author


""" Ф-ция возвращает словарь с заполненными случайным образом значениями ключа 'field'
 и значение ключа 'model' из импортируемой переменной MODEL"""

def field_() -> dict:
    Book['model'] = get_model()
    Book['fields']['title'] = get_book()
    Book['fields']['year'] = get_year()
    Book['fields']['pages'] = get_page()
    Book['fields']['rating'] = get_rating()
    Book['fields']['isbn13'] = get_isbn()
    Book['fields']['author'] = get_author()
    return Book


# Ф-ция генератор словаря, аргумент ф-ции - автоинкремент
def book_gen(start=1) -> dict:
    start_ = start
    while True:
        Book['pk'] = start_
        yield field_()
        start_ += 1


# Добавление словарей в список и запись списка в json
def main():
    list_ = []
    out = book_gen()
    for i in range(100):
        c = str(next(out))
        list_.append(c)

    with open('output.json', 'w', encoding='utf-8') as f:
        json.dump(list_, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    Book = book_init()
    main()
