class Singleton:

    def __init__(self,singleton_class):
        self._singleton_class = singleton_class

    def __call__(self):
        raise TypeError('Singletons are not callable')

    def instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._singleton_class()
            return self._instance
