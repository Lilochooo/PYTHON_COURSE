"""Module 04 — Solutions"""

# 1
def is_even(n):
    return n % 2 == 0

print(is_even(4), is_even(7))

# 2
def circle_area(radius, pi=3.14159):
    return pi * radius ** 2

print(circle_area(2))
print(circle_area(2, pi=3.14))

# 3
def stats(nums):
    return min(nums), max(nums), sum(nums) / len(nums)

low, high, avg = stats([3, 1, 4, 1, 5, 9])
print(low, high, avg)

# 4
def total(*nums):
    return sum(nums)

print(total(1, 2))
print(total(1, 2, 3, 4, 5))

# 5
def print_profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_profile(name="Ricky", major="Computer Engineering", year="junior")

# 6
def square(x):
    return x * x

def apply_twice(func, value):
    return func(func(value))

print(apply_twice(square, 3))

# 7
cubes = list(map(lambda x: x ** 3, [1, 2, 3, 4, 5]))
print(cubes)
