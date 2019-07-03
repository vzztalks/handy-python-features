class PrivateMethodException(Exception):
    pass

def private_function(function):
    def run_if_permitted(*args,**kwargs):
        if str(function.__name__).startswith("_"):
            raise PrivateMethodException()
        else:
            function(*args,**kwargs)
    return run_if_permitted

