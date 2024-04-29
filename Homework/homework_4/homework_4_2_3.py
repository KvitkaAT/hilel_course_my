given_list = [0, 1, 7, 2, 4, 8]
result = sum(given_list[::2]) * given_list[-1] if given_list else 0  # if the list is not empty, else = 0
print(result)
