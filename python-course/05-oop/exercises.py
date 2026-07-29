"""Module 05 — OOP"""

# TODO 1: Define a class `Rectangle` with __init__(self, width, height) that
# stores width and height. Add a method `area(self)` that returns
# width * height, and a method `perimeter(self)` that returns
# 2 * (width + height). Create an instance and print both.


# TODO 2: Add a method `is_square(self)` to Rectangle that returns True if
# width == height. Test it with a square and a non-square rectangle.


# TODO 3: Define a class `Circuit` with __init__(self, voltage, resistance).
# Add a method `current(self)` that returns voltage / resistance (Ohm's law).
# Create an instance with voltage=12, resistance=4 and print the current.


# TODO 4: Define a class `Vehicle` with __init__(self, make, model) storing
# both, and a method `describe(self)` that prints "make model".
# Then define a class `Car(Vehicle)` that inherits from Vehicle, adds
# num_doors in its __init__ (using super().__init__ for make/model), and
# overrides describe(self) to also print the number of doors.
# Create a Car instance and call describe().


# TODO 5: Define a class `Counter` with __init__(self) that sets count to 0,
# a method increment(self) that adds 1 to count, and a method value(self)
# that returns the current count. Create an instance, call increment()
# three times, then print value().
