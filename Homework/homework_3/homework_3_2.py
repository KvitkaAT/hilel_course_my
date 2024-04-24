given_list = [12, 3, 4, 10, 8]
if len(given_list) >= 1:  # list not empty
    given_list.insert(0, given_list.pop())
print(given_list)  # if list empty, print the given list

