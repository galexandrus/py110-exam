import json
import random
import faker
from conf import MODEL


def get_model() -> str:
    """
    Returns madel name from file conf.py

    :return: string
    """
    return MODEL


def get_title() -> str:
    """
    Returns random book title from file books.txt

    :return: string
    """
    with open("books.txt", encoding="utf-8") as titles_f:
        positions = titles_f.readline().split()
        pos = int(positions[random.randint(0, len(positions) - 1)])
        titles_f.seek(pos)
        title = titles_f.readline()
    return title.split("\n")[0]


def get_year() -> int:
    """
    Returns random year between 1500 and 2022 year, including both end points.

    :return: integer
    """
    min_year = 1500
    max_year = 2022
    return random.randint(min_year, max_year)


def get_pages() -> int:
    """
    Returns random pages count in book between 42 and 951 pages, including both end points.

    :return: integer
    """
    min_pages = 42
    max_pages = 951
    return random.randint(min_pages, max_pages)


def get_isbn() -> str:
    """
    Returns fake ISBN13 number of book.

    :return: string
    """
    fake_obj = faker.Faker("ru")
    fake_isbn = fake_obj.isbn13()
    return fake_isbn


def get_rating() -> float:
    """
    Returns random rating of book between 0 and 5, including both end points.

    :return: float
    """
    min_rating = 0
    max_rating = 500
    return random.randint(min_rating, max_rating) / 100


def get_price() -> float:
    """
    Returns random price of book between 10 and 900, including both end points.

    :return: float
    """
    min_price = 1000
    max_price = 90000
    return random.randint(min_price, max_price) / 100


def get_authors() -> list:
    """
    Generate a list of fake authors with Faker package.

    :return: list
    """
    authors = []
    fake_obj = faker.Faker("ru")
    for _ in range(random.randint(1, 3)):
        if random.randint(0, 1) == 1:
            first_name = fake_obj.first_name_male()
            last_name = fake_obj.last_name_male()
        else:
            first_name = fake_obj.first_name_female()
            last_name = fake_obj.last_name_female()
        authors.append(first_name + " " + last_name)
    return authors


def book_generator(start_pk: int = 1, book_count: int = 5) -> dict:
    """
    Generate a dictionary of fake books.

    :param start_pk: start value of autoincrement
    :param book_count: set count of books
    :return: dictionary
    """
    pk = start_pk
    for _ in range(1, book_count + 1):
        book_dict = {
            "model": get_model(),
            "pk": pk,
            "fields": {
                "title": get_title(),
                "year": get_year(),
                "pages": get_pages(),
                "isbn13": get_isbn(),
                "rating": get_rating(),
                "price": get_price(),
                "author": get_authors()
            }
        }
        yield book_dict
        pk += 1


if __name__ == '__main__':
    books = book_generator(start_pk=1, book_count=100)
    with open("books.json", "w", encoding="utf-8") as books_write_f:
        json.dump([book for book in books],
                  books_write_f,
                  ensure_ascii=False,
                  indent=4)
