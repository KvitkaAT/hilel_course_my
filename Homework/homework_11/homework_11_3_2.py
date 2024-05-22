def is_even(number: int) -> bool:
    if str(number)[-1] in "02468":  # converts number to string and checks the last digit
        return True  # returns true if the last digit is even
    return False  # returns false if the last digit is not even


if __name__ == "__main__":
    assert is_even(2494563894038**2) == True
    assert is_even(1056897**2) == False
    assert is_even(24945638940387**3) == False
    print("Ok")
