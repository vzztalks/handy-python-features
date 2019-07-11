import example_app.decorators_demo as decorators_demo



def run():
    try:
        print("\ndecorators_demo.private_function_check")
        decorators_demo.private_function_check()
    except Exception as e:
        print(e)

    try:
        print("\ndecorators_demo.singleton_check")
        decorators_demo.singleton_check()
    except Exception as e:
        print(e)

