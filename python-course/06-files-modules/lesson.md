# 06 — Files and Modules

## Reading and writing files

C requires `fopen`, checking for `NULL`, and `fclose` when you're done.
Python's `with` statement handles opening and closing for you automatically
(even if an error occurs partway through):

```python
# writing
with open("notes.txt", "w") as f:
    f.write("Hello, file\n")
    f.write("Second line\n")

# reading — whole file
with open("notes.txt", "r") as f:
    contents = f.read()
    print(contents)

# reading — line by line
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())   # .strip() removes the trailing newline
```

File modes: `"r"` read, `"w"` write (overwrites), `"a"` append.

No manual buffer allocation, no `fgets` with a size argument, no explicit
`fclose()` — the `with` block closes the file automatically when it ends.

## Working with CSV-like data

```python
with open("grades.csv", "r") as f:
    for line in f:
        fields = line.strip().split(",")
        print(fields)
```

`.split(",")` breaks a string into a list on the delimiter — very common
for parsing simple structured text.

## Modules — Python's version of separate .c/.h files

Any `.py` file is a module. If you have `helpers.py`:

```python
# helpers.py
def square(x):
    return x * x
```

You can use it from another file in the same folder:

```python
# main.py
import helpers

print(helpers.square(5))

# or import specific names directly
from helpers import square
print(square(5))
```

No header files, no separate declaration/definition split — a `.py` file
is both at once. `import` is roughly equivalent to `#include`, but it
imports actual runnable code, not just declarations.

## The standard library

Python ships with a lot built in — no separate installation needed:

```python
import math
print(math.sqrt(16))
print(math.pi)

import random
print(random.randint(1, 10))

import os
print(os.getcwd())   # current working directory
```

## Third-party packages

For anything not built in, `pip` is Python's package manager (roughly like
apt for Ubuntu packages, but for Python libraries):

```bash
pip install requests
```

```python
import requests
```

Now open `exercises.py`.
