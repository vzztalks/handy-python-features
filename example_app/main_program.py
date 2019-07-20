import example_app.decorators_demo as decorators_demo
import example_app.iterators_demo as iterators_demo
import example_app.generators_demo as generators_demo


def run():
    try:
        print("\n# decorators_demo.private_function_check")
        decorators_demo.private_function_check()
    except Exception as e:
        print(e)

    try:
        print("\n# decorators_demo.singleton_check")
        decorators_demo.singleton_check()
    except Exception as e:
        print(e)

    try:
        print("\n# iterators_demo.iterator_check")
        iterators_demo.iterator_check()
    except Exception as e:
        print(e)

    try:
        print("\n# iterators_demo.iterator_save_memory_check")
        iterators_demo.iterator_save_memory_check()
    except Exception as e:
        print(e)

    try:
        print("\n# generators_demo.generator_check")
        generators_demo.generator_check()
    except Exception as e:
        print(e)