"""Module 04 — Functions"""

# TODO 1: Write a function `is_even(n)` that returns True if n is even,
# False otherwise. Test it on 4 and 7.
#def is_even(n):
#    return n % 2 ==0
#print(is_even(4),is_even(8))

# TODO 2: Write a function `circle_area(radius, pi=3.14159)` with a default
# value for pi. Call it once with just a radius, and once overriding pi.
#def circle_area(radius,pi=3.14159):
#    return pi*radius**2
#print(circle_area(2))
#print(circle_area(2,pi=3.14))

# TODO 3: Write a function `stats(nums)` that returns a tuple of
# (minimum, maximum, average) for a list of numbers. Unpack the result
# into three variables when you call it.
#def stats(nums):
#    return min(nums),max(nums),sum(nums)/len(nums)
#low,high,avg= stats([2,3,7,1,7,8,3,6])
#print(low,high,avg)


# TODO 4: Write a function `total(*nums)` that accepts any number of
# positional arguments and returns their sum. Test with 2 args and with 5.
#def total(*nums):
#    return sum(nums)
#print(total(1 ,2))
#print(total(1,2,3,4,5))

# TODO 5: Write a function `print_profile(**info)` that accepts keyword
# arguments and prints each one as "key: value". Call it with name, major,
# and year.
#def print_profile(**info):
#    for key, val in info.items():
#        print(f"{key}: {val}")
#print_profile(name="Ricky",major="CE",year="Senior")
# TODO 6: Write a function `apply_twice(func, value)` that applies a given
# function to a value two times in a row and returns the result.
# Example: apply_twice(square, 3) -> square(square(3)) -> 81
# Define a `square` function to test it with.
#def square(x):
 #   return x*x
#def apply_twice(funct,value):
#    return funct(funct(value))
#print(apply_twice(square, 2 ))



# TODO 7: Using a lambda and map(), create a new list `cubes` that contains
# the cube of every number in [1, 2, 3, 4, 5].
cubes =list(map(lambda x: x*x*x, [1,2,3,4,5]))
print(cubes)
