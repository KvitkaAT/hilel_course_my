given_list = []
if len(given_list) % 2 == 0:  # even number of elements in the list
    middle_element = len(given_list) // 2
    divided_list_1 = given_list[:middle_element]  # from the first element up to the middle element
    divided_list_2 = given_list[middle_element:]  # from the middle element to the last element
else:  # odd number of elements in the list or empty list
    middle_element = len(given_list) // 2 + 1
    divided_list_1 = given_list[:middle_element]  # from first element to the middle element (including it)
    divided_list_2 = given_list[middle_element:]  # from the middle element (excluding it) to the last element
print([divided_list_1] + [divided_list_2])