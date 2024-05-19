def counter(func):  # the outer function that counts the number of calls
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Call {count} of {func.__name__}")
        return count

    return wrapper


@counter
def example_function():
    print("Inside the function")


example_function()
example_function()
example_function()