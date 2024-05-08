import random


def common_elements() -> set:
    random_divisible_3 = [digit for digit in range(random.randint(1, 1000)) if digit % 3 == 0]
    # list of random numbers divisible by 3
    random_divisible_5 = [digit for digit in range(random.randint(1, 2000)) if digit % 5 == 0]
    # list of random numbers divisible by 5
    return set(random_divisible_3).intersection(random_divisible_5)  # set of intersection numbers from both lists


if __name__ == "__main__":
    print(common_elements())
