from .book import Book


def private_function_check():

    book = Book("Five on a Treasure Island","Enid Blyton",300);

    book.print_description()

    book._get_name()
    # book._get_author()
    # book._get_page_count()