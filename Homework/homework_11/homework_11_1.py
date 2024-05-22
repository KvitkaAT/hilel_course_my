from inspect import isgenerator


def prime_number(n):
    if n <= 1:  # if a number is <= 1, it is not prime
        return False
    for divisor in range(2, int(n ** 0.5) + 1):  # loops within the range of 2 and square roots of the number
        if n % divisor == 0:  # if n is divisible by number from the range, it is not prime
            return False
    return True


def prime_generator(end: int) -> list:  # generates list of prime numbers
    for number in range(2, end + 1):  # loops within the range of 2 and the last number inclusively
        if prime_number(number):  # if the number is prime, adds to the list
            yield number


gen = prime_generator(1)


if __name__ == "__main__":
    assert isgenerator(gen) == True
    assert list(prime_generator(10)) == [2, 3, 5, 7]
    assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13]
    assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    print('Ok')
