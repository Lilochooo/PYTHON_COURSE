# 01 — Basics

## No compiler, no main()

C needs `gcc program.c -o program` then `./program`. Python just runs:

```bash
python hello.py
```

There's no `int main(void) { ... return 0; }` wrapper. The file itself
is the program, top to bottom.

```python
print("Hello, world")
```

That's the whole program.

## Variables: no types, no declarations

In C:
```c
int x = 5;
float y = 3.14;
char name[] = "Ricky";
```

In Python:
```python
x = 5
y = 3.14
name = "Ricky"
```

You never declare a type. `x` doesn't have a type — the *value* `5` has a
type (`int`). You can rebind `x` to a string later and Python won't stop you:

```python
x = 5
x = "now I'm a string"   # totally legal, if a bit chaotic
```

This is called **dynamic typing**. It's more flexible and more forgiving, but
it also means the interpreter won't catch type mistakes at compile time —
they show up at runtime instead. `type(x)` tells you what something currently
is.

## Indentation is syntax, not style

C uses `{ }` to mark blocks. Python uses indentation — consistently, or the
program won't run:

```python
if x > 0:
    print("positive")
    print("still inside the if")
print("outside the if")
```

No braces, no semicolons. The colon `:` starts a block; indentation (use 4
spaces, always) marks what's inside it.

## Core types

| C | Python |
|---|---|
| `int` | `int` (arbitrary precision — no overflow at 2^31) |
| `float`, `double` | `float` |
| `char[]` / `char*` | `str` |
| no built-in equivalent | `bool` (`True`/`False`, capitalized) |
| `NULL` | `None` |

Strings are a big upgrade from C's `char` arrays — no null terminators, no
manual buffer sizing, and lots of built-in operations:

```python
name = "Ricky"
print(len(name))          # 5 — length, no strlen()
print(name.upper())       # "RICKY"
print(name + " Torres")   # concatenation with +
print(f"Hi, {name}!")     # f-strings: variable interpolation, like a safer printf
```

That last one — the f-string — replaces most of what you'd reach for
`printf`/`sprintf` for. `f"{x}"` drops `x` in as text; `f"{x:.2f}"` formats
a float to 2 decimal places, same idea as `%.2f`.

## Input

```python
name = input("What's your name? ")   # always returns a string
age = int(input("Age: "))            # convert manually, like atoi()
```

No `scanf` format specifiers — `input()` always gives you a string, and you
convert it (`int()`, `float()`) yourself when you need a number.

## Comments

```python
# single line, like //
"""
multi-line,
often used for documentation
"""
```

## What Python does NOT make you do

- No header files, no `#include`
- No semicolons
- No manual memory management — Python garbage collects for you
- No pointers to manage — you'll see references, but no `*`/`&`/`malloc`/`free`

Now open `exercises.py`.
