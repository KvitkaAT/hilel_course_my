class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"{self.name}: ${self.price}, {self.description}, {self.dimensions}."


lemon = Item("lemon", 5, "yellow", "small")
apple = Item("apple", 2, "red", "middle")
print(lemon)
print(apple)


class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}, {self.numberphone}."


buyer = User("John", "Snow", "1-800-790-55-77")
print(buyer)


class Purchase:
    def __init__(self, user):
        self.products = {}  # creates a dictionary of items and their amount
        self.user = user
        self.total = 0  # sets the total to zero

    def add_item(self, item, cnt):
        self.products[item] = cnt  # adds a new key-value to the dictionary

    def __str__(self):
        items_str = "".join(f"{item.name}: {cnt}\n" for item, cnt in self.products.items())
        # iterates over key-value pair in self.products
        items_str = items_str.rstrip()  # deletes the empty line at the end
        return f"Buyer: {self.user.name} {self.user.surname}\nItems:\n{items_str}"  # returns the formatted string

    def get_total(self):
        self.total = sum(item.price * cnt for item, cnt in self.products.items())  # calculates the total of order
        return self.total


cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
total_cost = cart.get_total()
print(cart)
print("Total:", total_cost)


if __name__ == "__main__":
    assert isinstance(cart.user, User) is True
    assert cart.get_total() == 60
    assert cart.get_total() == 60
    cart.add_item(apple, 10)
    print(cart)

    assert cart.get_total() == 40
