def closure_example(x):
    """
    Реалізує функцію, яка використовує замикання для збереження значення.

    :param x: Початкове значення.
    :return: Функція, яка використовує замикання для збереження значення x.
    """
    def inner_function(y):
        nonlocal x
        x += y
        return x

    return inner_function


closure_instance = closure_example(10)
result_1 = closure_instance(2)
result_2 = closure_instance(5)


