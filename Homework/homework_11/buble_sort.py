def bubble_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Перевірка
assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
assert bubble_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]
assert bubble_sort([3, 8, 1, 7, 2, 9, 6]) == [1, 2, 3, 6, 7, 8, 9]
print("Ok")