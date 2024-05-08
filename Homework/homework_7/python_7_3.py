def second_index(text: str, some_str: str) -> int | None:
    index_one = text.find(some_str)
    if index_one == -1:
        return None
    index_two = text.find(some_str, index_one + 1)
    if index_two == -1:
        return None
    return index_two


if __name__ == "__main__":
    assert second_index("sims", "s") == 3
    assert second_index("find the river", "e") == 12
    assert second_index("hi", "h") is None
    assert second_index("Hello, hello", "lo") == 10
    assert second_index("anndfdfd", "a") is None
    print('ОК')
