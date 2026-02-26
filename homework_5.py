class Distance:
    conversion_dict = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000
    }

    def convert(self):
        if self.unit not in Distance.conversion_dict:
            raise ValueError(f"Unknown unit: {self.unit}")
        return self.value * Distance.conversion_dict[self.unit]

    def __init__(self, value, unit):
        if unit not in Distance.conversion_dict:
            raise ValueError(f"Unsupported unit: {unit}")
        if value < 0:
            raise ValueError("Distance cannot be negative")
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"

    def __add__(self, other):
        if not isinstance(other, Distance):
            raise TypeError("Can only add Distance to Distance")

        total_in_meters = self.convert() + other.convert()

        new_value = total_in_meters / Distance.conversion_dict[self.unit]
        return Distance(new_value, self.unit)

    def __sub__(self, other):
        if not isinstance(other, Distance):
            raise TypeError("Can only subtract Distance from Distance")

        result_in_meters = self.convert() - other.convert()

        if result_in_meters < 0:
            raise ValueError("Resulting distance cannot be negative")

        new_value = result_in_meters / Distance.conversion_dict[self.unit]
        return Distance(new_value, self.unit)


    def __eq__(self, other):
        return self.convert() == other.convert()

    def __lt__(self, other):
        return self.convert() < other.convert()

    def __le__(self, other):
        return self.convert() <= other.convert()

    def __gt__(self, other):
        return self.convert() > other.convert()

    def __ge__(self, other):
        return self.convert() >= other.convert()




d1 = Distance(10, "m")
d2 = Distance(2, "km")
d3 = Distance(500, "cm")

print("Инициализация:")
print(d1)
print(d2)
print(d3)

print("\nСложение:")
print(d1 + d2)
print(d2 + d1)

print("\nВычитание:")
print(d2 - d1)

print("\nСравнение:")
print(d1 == d3)
print(d1 < d2)
print(d2 > d1)