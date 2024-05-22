from inspect import isgenerator


def generate_cube_numbers(end: int):
    number = 2  # generator starting point
    while number ** 3 <= end:  # while number***3 is less than the last number
        yield number ** 3  # adds the number cube to the list
        number += 1  # goes to the next number


gen = generate_cube_numbers(1)


if __name__ == "__main__":
    assert isgenerator(gen) == True
    assert list(generate_cube_numbers(10)) == [8]
    assert list(generate_cube_numbers(100)) == [8, 27, 64]
    assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000]
    print("Ok")

