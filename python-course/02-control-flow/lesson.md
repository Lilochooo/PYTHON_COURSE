# 02 — Control Flow

## if / elif / else

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

print(grade)
```

Same logic as C's `if`/`else if`/`else`, just `elif` instead of `else if`,
no parentheses required around the condition, and a colon + indentation
instead of braces.

Booleans use words, not symbols:

| C | Python |
|---|---|
| `&&` | `and` |
| `\|\|` | `or` |
| `!` | `not` |
| `==`, `!=` | same |

```python
if age >= 18 and has_id:
    print("allowed")
```

## while loops

```python
count = 0
while count < 5:
    print(count)
    count += 1   # no ++ in Python — use += 1
```

Note: **no `count++` or `++count`**. Python doesn't have the increment
operator. `count += 1` is the idiom.

## for loops — this is the big difference from C

C's `for` loop is index-based:
```c
for (int i = 0; i < 10; i++) {
    printf("%d\n", i);
}
```

Python's `for` loop iterates over a **sequence** directly. To get the C-style
counting loop, you use `range()`:

```python
for i in range(10):       # 0,1,2,...,9 — like C's i < 10
    print(i)

for i in range(2, 10):    # start=2, stop=10 (exclusive)
    print(i)

for i in range(0, 10, 2): # start, stop, step — evens 0,2,4,6,8
    print(i)
```

But Python's `for` really shines when you loop over actual data, not just
indices — you'll use this constantly once you hit lists in Module 3:

```python
names = ["Alice", "Bob", "Carla"]
for name in names:
    print(name)
```

No manual indexing (`names[i]`), no off-by-one risk. If you need the index
*and* the value, use `enumerate()`:

```python
for i, name in enumerate(names):
    print(i, name)
```

## break / continue

Same as C:

```python
for i in range(10):
    if i == 5:
        break        # exit the loop entirely
    if i % 2 == 0:
        continue     # skip to next iteration
    print(i)
```

## Truthiness

Python doesn't require an explicit `== 0` check. Empty things are falsy:

```python
name = ""
if not name:
    print("empty string")

items = []
if not items:
    print("empty list")
```

`0`, `0.0`, `""`, `[]`, `{}`, `None`, and `False` are all falsy. Everything
else is truthy. This is different from C, where you'd typically compare
explicitly (`if (strlen(name) == 0)`).

Now open `exercises.py`.
