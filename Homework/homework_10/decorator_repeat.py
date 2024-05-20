def repeat_decorator(repeat_count):
    """
    Реалізує декоратор, який повторює виклик функції задану кількість разів.

    :param repeat_count: Кількість повторень.
    :return: Декоратор для повторюваного виклику функції.
    """

    def decorator(func):
        def inner_function(*args, **kwargs):
            if repeat_count > 0:
                for count in range(repeat_count):
                    func(*args, **kwargs)
            else:
                print("None")
        return inner_function

    return decorator


@repeat_decorator(0)
def example_function():
    print("Function called")


assert example_function() is None