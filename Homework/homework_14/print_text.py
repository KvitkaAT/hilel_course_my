from pathlib import Path
class Print:
    def print_text(self, text):
        pass


class PrintToScreen(Print):
    def print_text(self, text):
        print(text) == print_screen


class PrintToFile(Print):
    def __init__(self, filename):
        self.filename = filename

    def print_text(self, text):
        with open("output.txt", "a") as file:
            file.write(text)
        print(text) == print_file


print_screen = PrintToScreen()
print_file = PrintToFile("output.txt")

print_screen.print_text("Hello, world!")
print_file.print_text("This text goes to a file.")