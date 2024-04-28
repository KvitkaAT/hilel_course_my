import random  # imports random method
given_list = []  # creates an empty list
for element in range(1, 100):
    if element % 3 == 0 and element % 5 == 0:  # if an element is divided by 3 and 5
        given_list.append("FizzBuzz")  # adds FizzBuzz to the list
    elif element % 3 == 0:  # if an element is divided by 3
        given_list.append("Fizz")  # adds Fizz to the list
    elif element % 5 == 0:  # if an element is divided by 5
        given_list.append("Buzz")  # adds Buzz to the list
    else:  # for all other elements
        given_list.append(element)  # adds the element to the list
print(given_list)


