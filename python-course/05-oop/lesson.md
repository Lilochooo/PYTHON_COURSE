# 05 — Object-Oriented Programming

## From struct to class

In C, you'd bundle related data into a struct and write separate functions
that take the struct as a parameter:

```c
struct Student {
    char name[50];
    float gpa;
};

void print_student(struct Student s) {
    printf("%s: %.2f\n", s.name, s.gpa);
}
```

Python's `class` bundles the data *and* the functions that operate on it
together:

```python
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def print_info(self):
        print(f"{self.name}: {self.gpa:.2f}")

s = Student("Ricky", 3.8)
s.print_info()
```

- `__init__` is the constructor — runs automatically when you create an
  instance (`Student("Ricky", 3.8)`).
- `self` refers to the specific instance — it's always the first parameter
  of a method, and Python passes it automatically. Think of it as an
  implicit pointer to "this particular struct," except you don't write the
  `&`/`*`.
- `self.name = name` stores `name` as an attribute on that instance.

## Creating multiple instances

```python
s1 = Student("Ricky", 3.8)
s2 = Student("Alex", 3.5)
# each has its own independent name and gpa
```

## Methods vs. attributes

- **Attributes** = data (`self.name`, `self.gpa`) — like struct fields
- **Methods** = functions defined inside the class that act on that data

```python
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def is_honor_roll(self):
        return self.gpa >= 3.5
```

## Inheritance

A class can extend another, inheriting its attributes and methods:

```python
class GradStudent(Student):
    def __init__(self, name, gpa, thesis_title):
        super().__init__(name, gpa)   # call the parent's __init__
        self.thesis_title = thesis_title

    def print_info(self):             # override the parent's method
        print(f"{self.name} ({self.thesis_title}): {self.gpa:.2f}")
```

`super().__init__(...)` calls the parent class's constructor so you don't
have to repeat that setup code.

## Why bother with classes at all?

For small scripts, plain functions and dicts are often enough. Classes earn
their keep once you have several pieces of related data and behavior that
naturally travel together, and especially once you want multiple
independent instances of "the same kind of thing" (multiple students,
multiple bank accounts, multiple game entities, etc.).

Now open `exercises.py`.
