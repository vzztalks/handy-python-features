import inspect


class PrivateFunctionError(Exception):
    def __init__(self):
        super().__init__(self, "This is a private function and should not be called by outside")


def private_function(function):
    def run_if_not_private(*args, **kwargs):
        caller = inspect.stack()[1][4][0].strip()
        print("Caller : {}".format(caller))
        if ("self." + function.__name__) in caller:
            return function(*args, **kwargs)
        else:
            raise PrivateFunctionError()

    return run_if_not_private
