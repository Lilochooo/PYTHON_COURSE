"""Module 02 — Control Flow"""

# TODO 1: Write an if/elif/else that takes a variable `temp = 95` and prints
# "hot" if temp >= 90, "warm" if temp >= 70, else "cold".
temp = 69
if temp >= 90:
    print("hot")
elif temp >= 70:
    print("warm")
else:    print("cold")


# TODO 2: Use a while loop to print numbers 10 down to 1 (countdown), then
# print "liftoff" after the loop ends.
count=10
while count > 0:
    print(count)
    count -= 1
print("liftoff!!")

# TODO 3: Use range() in a for loop to print all even numbers from 0 to 20
# (inclusive of 20).
for i in range(0, 21, 2):
    print(i)


# TODO 4: Given the list below, loop over it directly (no indexing) and
# print each item in uppercase.
courses = ["ece2303", "cs1301", "math2414", "ce2326"]
for course in courses:
    print(course.upper())

# TODO 5: Using enumerate(), loop over `courses` above and print each item
# with its position, 1-indexed, like: "1: ece2303"
for i, course in enumerate(courses, start=1):
    print(f"{i}: {course.upper()}")

# TODO 6: Loop from 1 to 100 using range(). Use continue to skip numbers not
# divisible by 7, and print the ones that are.
for i in range(1,101):
    if i % 7 != 0:
        continue
    print(i)

# TODO 7: Write a loop over range(20) that breaks as soon as it finds a
# number greater than 15, and prints that number.
for i in range(20):
    if i > 15:
        print(i)
        break