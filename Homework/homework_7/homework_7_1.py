def say_hi(name: str, age: int) -> str:
    return f"Hi. My name is {name} and I'm {age} years old"


if __name__ == "__main__":
    assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old"
    assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old"
    assert say_hi("Anna", 41) == "Hi. My name is Anna and I'm 41 years old"
    assert say_hi("Eveline-Kathrine", 200) == "Hi. My name is Eveline-Kathrine and I'm 200 years old"
    print('ОК')
