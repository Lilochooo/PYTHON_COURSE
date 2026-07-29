# 07 — Mini Projects

You've now covered variables, control flow, data structures, functions,
classes, and files. These projects combine everything. Pick one, build it
in a new `.py` file in this folder, and don't look at any solution — there
isn't one provided. Struggling through the design decisions is the point.

## 1. Grade Calculator
Read a list of (course, credit_hours, grade) from a CSV file you create,
compute a GPA (standard 4.0 scale), and print a report. Combines: file
reading, dicts/lists, functions.

## 2. Student Record System
Build a `Student` class with name, courses (a list), and a method to add a
course and compute average grade. Create several students, store them in a
list, and write a function that finds the student with the highest average.
Combines: classes, lists, functions.

## 3. Simple Circuit Analyzer
Build a `Resistor` class (resistance) and a `Circuit` class that holds a
list of resistors in series (sum resistance) or parallel (reciprocal sum).
Add a method to compute total current given a voltage. Combines: classes,
OOP composition (a Circuit *has* Resistors), basic physics you already know
from ECE-2303.

## 4. Word Frequency Counter
Read a text file, split it into words, and use a dict to count how many
times each word appears. Print the 5 most common words. Combines: files,
dicts, string methods.

## 5. Command-Line To-Do List
Use a loop with `input()` to let the user add tasks, mark them done, and
list them, storing tasks as a list of dicts (`{"task": ..., "done": False}`).
Save/load the list to a file so it persists between runs. Combines:
everything — loops, dicts, files, functions.

## If you want to push further
Once one of these feels solid, try opening it in Cursor and using the
inline chat to ask for a code review — not to write it for you, but to
point out where your code could be more idiomatic Python (e.g. "should
this loop be a list comprehension?").
