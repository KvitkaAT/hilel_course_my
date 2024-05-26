import io
import sys


class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")


class C(A):
    def show(self):
        print("C")


class D(B, C):
    def show(self):
        print("D")


def capture_stdout(func):
    """Capture the stdout output of a function"""
    captured_output = io.StringIO()          # Create StringIO object
    sys.stdout = captured_output             # Redirect stdout.
    func()                                   # Call function.
    sys.stdout = sys.__stdout__              # Reset redirect.
    return captured_output.getvalue().strip()  # Return captured output.


# Перевірка
obj_A = A()
output_A = capture_stdout(obj_A.show)
assert output_A == "A"