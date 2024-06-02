class TemperatureValueError(Exception):
    pass


class TemperatureConverter:
    def convert_celsius_to_fahrenheit(self, celsius: float) -> float | str:
        if celsius <= -237:
            raise TemperatureValueError("Invalid temperature value")
        fahrenheit = (celsius * 9 / 5) + 32
        return fahrenheit
