given_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 0, 96, 0]
list_zero = [element for element in given_list if element == 0]  # creates a list with zeroes only
list_zerofree = [element for element in given_list if element != 0]  # creates a list without zeroes
print(list_zerofree + list_zero)  # adds a list with zeroes at the end of the list without zeroes
