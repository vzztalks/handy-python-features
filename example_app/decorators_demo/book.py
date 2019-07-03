from handy_features import private_function

class Book:

    def __init__(self, name, author, page_count):
        self._name = name
        self._author = author
        self._page_count = page_count

    def print_description(self):
        print(
            "The book '{}' written by {} has {} pages. "
                .format(
                self._book_name(),
                self._author(),
                self._page_count()
            )
        )

    @private_function
    def _book_name(self):
        pass

    @private_function
    def _author(self):
        pass

    @private_function
    def _page_count(self):
        pass
