"""Module 03 — Data Structures"""

# TODO 1: Create a list `grades = [90, 85, 77, 92, 68]`. Append 100 to it,
# remove 77, then print the final list and its length.
grades = [90, 85, 77, 92, 68]
grades.append(100)
grades.remove(77)
print(grades)
print(len(grades))
# TODO 2: Using slicing, print the first 3 elements of `grades`, then the
# last 2, then the whole list reversed.
print(grades[:3])
print(grades[3:])
print(grades[::-1])
# TODO 3: Use a list comprehension to build a list of the squares of
# 1 through 15.
square = [x**2 for x in range(1,16)]
print(square)

# TODO 4: Use a list comprehension to build a list of only the grades from
# `grades` (from TODO 1, before you modify it further) that are >= 80.
b = [x for x in grades if x >=80]
print(b)

# TODO 5: Create a dict `student` with keys "name", "major", "year" and
# your own values. Print each key-value pair using .items(). Then add a
# new key "gpa" and print the updated dict.
student ={
    "name": "Ricky",
    "major": "Computer Engineeing",
    "year": "Senior"
}
for key, value in student.items():
        print(key, value)
student["gpa"]= "3.7"
for key, value in student.items():
        print(key, value)

# TODO 6: Create a set from this list: [1, 2, 2, 3, 4, 4, 4, 5]. Print the
# set, then check whether 3 is in it and whether 10 is in it.
set = { 1, 2, 2, 3, 4, 4, 4, 5}
print(set)
print(3 in set)
print(10 in set)


# TODO 7: Write a function `double_all(lst)` that takes a list and doubles
# every element IN PLACE (modifies the original list, doesn't return a new
# one) — hint: use a for loop with enumerate() and index assignment
# lst[i] = ...
def double_all(lst):
    for i, val in enumerate(lst):
        lst[i] = val * 2
nums=[1,2,3]
double_all(nums)
print(nums)