class Counter:

    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start: int) -> None:
        self.current = start

    def set_max(self, max_max: int) -> None:
        self.max_value = max_max

    def set_min(self, min_min: int) -> None:
        self.min_value = min_min

    def step_up(self) -> None:
        if self.current >= self.max_value:
            raise ValueError("The maximum value has been reached.")
        self.current += 1

    def step_down(self) -> None:
        if self.current <= self.min_value:
            raise ValueError("The minimum value has been reached.")
        self.current -= 1

    def get_current(self) -> int:
        return self.current


counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()


if __name__ == "__main__":
    assert counter.get_current() == 10
    try:
        counter.step_up()  # ValueError
    except ValueError as e:
        print(e)  # Достигнут максимум
    assert counter.get_current() == 10

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()


if __name__ == "__main__":
    assert counter.get_current() == 7
    try:
        counter.step_down()  # ValueError
    except ValueError as e:
        print(e)  # Достигнут минимум
    assert counter.get_current() == 7
