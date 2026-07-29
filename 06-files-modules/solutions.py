"""Module 06 — Solutions (run from this folder so file paths resolve)"""

import math
import random
from helper import add  # requires helper.py's add() to be filled in

# 1
with open("scratch.txt", "w") as f:
    f.write("line one\n")
    f.write("line two\n")
    f.write("line three\n")

# 2
with open("scratch.txt", "r") as f:
    print(f.read())

# 3
with open("scratch.txt", "r") as f:
    for line in f:
        print(line.strip())

# 4
with open("grades.csv", "w") as f:
    f.write("math,90\n")
    f.write("science,85\n")
    f.write("ce,95\n")

with open("grades.csv", "r") as f:
    for line in f:
        subject, grade = line.strip().split(",")
        print(subject, grade)

# 5
print(add(3, 4))

# 6
print(math.sqrt(144))
print(f"{math.pi:.4f}")

# 7
for _ in range(5):
    print(random.randint(1, 100))
