import random  # imports random method
random_list = [element for element in range(random.randint(3, 10))]  # creates a list of random elements 3:10
new_list = [random_list[0], random_list[2], random_list[-2]]  # creates a new list of elements with specific indexes
print(random_list)
print(new_list)
