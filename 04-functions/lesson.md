# 04 — Functions

## Defining a function

```python
def add(a, b):
    return a + b

result = add(3, 4)
```

No return type or parameter types declared — Python figures it out at
runtime. Compare to C:

```c
int add(int a, int b) {
    return a + b;
}
```

You *can* add type hints for clarity (and Cursor/editors will use them for
better autocomplete), but Python doesn't enforce them:

```python
def add(a: int, b: int) -> int:
    return a + b
```

## Default arguments

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Ricky")                    # "Hello, Ricky!"
greet("Ricky", greeting="Hey")    # "Hey, Ricky!"
```

No function overloading needed for "optional" parameters like you might
fake in C with a sentinel value.

## Returning multiple values

C makes you return a struct or use output pointers to return more than one
value. Python just lets you return a tuple:

```python
def min_max(nums):
    return min(nums), max(nums)

low, high = min_max([3, 1, 4, 1, 5])
```

## *args and **kwargs — variable numbers of arguments

```python
def total(*nums):          # collects any number of positional args into a tuple
    return sum(nums)

total(1, 2, 3)              # 6
total(1, 2, 3, 4, 5)        # 15

def describe(**info):       # collects keyword args into a dict
    for key, val in info.items():
        print(f"{key}: {val}")

describe(name="Ricky", major="CE")
```

## Scope

Same lexical scoping idea as C — a variable defined inside a function
doesn't leak out. The difference: to *modify* a variable from an enclosing
scope inside a function, you need the `global` keyword (rare, usually a
sign to restructure instead):

```python
counter = 0

def increment():
    global counter
    counter += 1
```

Without `global`, Python would treat `counter` inside the function as a new
local variable.

## Functions are values

You can pass functions around like any other variable — no function
pointer syntax needed:

```python
def square(x):
    return x * x

def apply(func, value):
    return func(value)

print(apply(square, 5))   # 25
```

Also common: `lambda` for small, throwaway functions:

```python
square = lambda x: x * x
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x * x, nums))
```

Now open `exercises.py`.
