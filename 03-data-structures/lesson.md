# 03 — Data Structures

This is where Python replaces C's arrays and structs with more flexible
built-ins.

## Lists — like arrays, but resizable

```python
nums = [1, 2, 3, 4]
nums.append(5)          # grow it — no realloc needed
nums.insert(0, 0)       # insert at index
nums.remove(3)          # remove by value
nums.pop()               # remove & return last item
print(nums[0])           # indexing works like C
print(nums[-1])          # negative index = from the end
print(len(nums))         # length, no manual counter needed
```

Unlike a C array, a list can hold mixed types and grows/shrinks freely:

```python
mixed = [1, "two", 3.0, True]
```

**Slicing** — pulling out a sub-range, no loop needed:

```python
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])    # [1, 2, 3] — index 1 up to (not including) 4
print(nums[:3])     # [0, 1, 2] — from start
print(nums[3:])     # [3, 4, 5] — to end
print(nums[::-1])   # [5, 4, 3, 2, 1, 0] — reversed
```

**List comprehensions** — build a list from a loop, in one line:

```python
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
```

Read `[expression for item in iterable if condition]` left to right: "give
me `expression`, for each `item` in `iterable`, if `condition` holds."

## Tuples — like a list, but immutable

```python
point = (3, 4)
x, y = point   # unpacking — assigns 3 to x, 4 to y in one line
```

Use tuples for fixed-size groupings that shouldn't change (coordinates,
RGB values). Once created, you can't modify a tuple's contents.

## Dictionaries — Python's answer to a struct / hash map

C doesn't have a built-in hash map. Python's `dict` gives you key-value
lookup natively:

```python
student = {
    "name": "Ricky",
    "major": "Computer Engineering",
    "gpa": 3.8
}

print(student["name"])         # access by key
student["year"] = "junior"     # add a new key
del student["gpa"]             # remove a key

for key, value in student.items():
    print(key, value)
```

This replaces a lot of what you'd build a `struct` for in C — except a dict
is dynamic (keys can be added/removed at runtime) and doesn't need a
predefined layout.

## Sets — unique, unordered values

```python
seen = {1, 2, 2, 3, 3, 3}
print(seen)              # {1, 2, 3} — duplicates collapse automatically
print(2 in seen)         # membership test, O(1) average
```

Great for deduplication and fast membership checks, something you'd
normally write a loop for in C.

## Mutability — the thing that trips people up

Lists and dicts are **mutable** — passing them into a function and modifying
them modifies the original (similar in spirit to passing a pointer in C).
Strings, tuples, and numbers are **immutable** — you can't change them in
place, only create a new one.

```python
def add_item(lst):
    lst.append("new")   # modifies the caller's list

my_list = ["a", "b"]
add_item(my_list)
print(my_list)   # ["a", "b", "new"] — changed, no explicit pointer needed
```

Now open `exercises.py`.
