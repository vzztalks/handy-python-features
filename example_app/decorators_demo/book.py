from handy_features.decorators import private_function

class Book:

    def __init__(self, name, author, page_count):
        self._name = name
        self._author = author
        self._page_count = page_count

    def print_description(self):
        print("The book '{}' written by {} has {} pages. ".format(
            self._get_name(),
            self._get_author(),
            self._get_page_count()
        ))

    @private_function
    def _get_name(self):
        print(self._name)
        return str(self._name).upper()

    # @private_function
    def _get_author(self):
        print(self._author)
        return self._author

    # @private_function
    def _get_page_count(self):
        print(self._page_count)
        return self._page_count


