from .book import Book


def private_method_check():

    book = Book("Five on a Treasure Island","Enid Blyton",300);

    book.print_description()

    book._book_name()
    book._author()
    book._page_count()