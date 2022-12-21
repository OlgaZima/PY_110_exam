import random
import json
from faker import Faker
from conf import MODEL
fake = Faker()
Faker.seed(0)

Book = {"model": "shop_final.book",
        "pk": 1,
        "fields": {
            "title": "test_book",
            "year": 2020,
            "pages": 123,
            "isbn13": "978-1-60487-5",
            "rating": 5,
            "price": 123456.0,
            "author": ["test_author_1",
                       "test_author_2"]

        }}

def get_book():
    with open('books.txt', 'r', encoding="utf-8") as f:
        books = []
        for line in f:
            books.append(line.strip())
    return random.choice(books)


def get_year():
    return random.randrange(1900, 2022, 1)


def get_page():
    return random.randrange(1, 1000000, 1)


def get_rating():
    return random.uniform(0, 5)


def get_price():
    return random.uniform(0, 10000)


def get_isbn():
    return fake.isbn13()


def get_author():
    return fake.name()



def field_() -> dict:
    Book['fields']['title'] = get_book()
    Book['fields']['year'] = get_year()
    Book['fields']['pages'] = get_page()
    Book['fields']['rating'] = get_rating()
    Book['fields']['isbn13'] = get_isbn()
    Book['fields']['author'] = get_author()
    return Book


def book_gen(start=1):
    start_ = start
    while True:
        Book["pk"] = start_
        yield field_()
        start_ += 1


def main():
    list_ = []
    out = book_gen()
    for i in range(100):
        list_.append(next(out))
        with open('output.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(list_, indent=4))


if __name__ == "__main__":
    main()
    #my_first_gen = book_gen()
    #print(next(my_first_gen))
    #print(next(my_first_gen))




