def pow(x: int) -> int:
    return x ** 2


def some_gen(begin: int, end: int, func):
    """
     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності
    """
    number = begin
    for num in range(end):
        yield number
        number = func(number)


from inspect import isgenerator

gen = some_gen(2, 4, pow)


if __name__ == "__main__":
    assert isgenerator(gen) == True
    assert list(gen) == [2, 4, 16, 256]
    print('OK')
