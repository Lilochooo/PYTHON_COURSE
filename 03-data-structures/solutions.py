"""Module 03 — Solutions"""

# 1
grades = [90, 85, 77, 92, 68]
grades.append(100)
grades.remove(77)
print(grades, len(grades))

# 2
print(grades[:3])
print(grades[-2:])
print(grades[::-1])

# 3
squares = [x**2 for x in range(1, 16)]
print(squares)

# 4
high_grades = [g for g in grades if g >= 80]
print(high_grades)

# 5
student = {"name": "Ricky", "major": "Computer Engineering", "year": "junior"}
for key, value in student.items():
    print(key, value)
student["gpa"] = 3.8
print(student)

# 6
s = {1, 2, 2, 3, 4, 4, 4, 5}
print(s)
print(3 in s)
print(10 in s)

# 7
def double_all(lst):
    for i, val in enumerate(lst):
        lst[i] = val * 2

nums = [1, 2, 3]
double_all(nums)
print(nums)
