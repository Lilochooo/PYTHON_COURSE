"""Module 02 — Solutions"""

# 1
temp = 95
if temp >= 90:
    print("hot")
elif temp >= 70:
    print("warm")
else:
    print("cold")

# 2
count = 10
while count >= 1:
    print(count)
    count -= 1
print("liftoff")

# 3
for i in range(0, 21, 2):
    print(i)

# 4
courses = ["ece2303", "cs1301", "math2414", "ce2326"]
for c in courses:
    print(c.upper())

# 5
for i, c in enumerate(courses, start=1):
    print(f"{i}: {c}")

# 6
for i in range(1, 101):
    if i % 7 != 0:
        continue
    print(i)

# 7
for i in range(20):
    if i > 15:
        print(i)
        break
