"""Module 05 — Solutions"""

# 1 & 2
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

r = Rectangle(4, 6)
print(r.area(), r.perimeter())
print(r.is_square())
sq = Rectangle(5, 5)
print(sq.is_square())

# 3
class Circuit:
    def __init__(self, voltage, resistance):
        self.voltage = voltage
        self.resistance = resistance

    def current(self):
        return self.voltage / self.resistance

c = Circuit(12, 4)
print(c.current())

# 4
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        print(f"{self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def describe(self):
        print(f"{self.make} {self.model}, {self.num_doors} doors")

my_car = Car("Honda", "Civic", 4)
my_car.describe()

# 5
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def value(self):
        return self.count

ctr = Counter()
ctr.increment()
ctr.increment()
ctr.increment()
print(ctr.value())
