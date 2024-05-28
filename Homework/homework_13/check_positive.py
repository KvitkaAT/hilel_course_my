def check_positive(value: float):
    if value <= 0:
        raise ValueError("Value must be positive")


check_positive(5)
print("Ok")
check_positive(-4)
# try:
#     check_positive(5)
# except ValueError as e:
#     print("Test failed:", e)
#
# try:
#     check_positive(-3)
# except ValueError as e:
#     print("Test passed:", e)