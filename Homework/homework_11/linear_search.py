def linear_search(arr: list, target: int) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


if __name__ == "__main__":
    assert linear_search([11, 12, 22, 25, 34, 64, 90], 22) == 2
