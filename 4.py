#A Functions
# Functions are reusable blocks of code that perform specific tasks.

print("#A Functions")

def greet(name):
    """This function prints a greeting message."""
    return f"Hello, {name}!"

print(greet("Alice"))  # Calling the function

# Function with default parameters
def add_numbers(a, b=5):
    return a + b

print("Addition with default parameter:", add_numbers(10))  # Uses default b=5

# Function with variable-length arguments
def sum_all(*args):
    return sum(args)

print("Sum of all numbers:", sum_all(1, 2, 3, 4, 5))  # Passes multiple arguments

# Function with keyword arguments
def person_info(name, age):
    return f"Name: {name}, Age: {age}"

print(person_info(age=30, name="Bob"))  # Keyword arguments allow flexible ordering

#B Lambda Expressions
# Lambda functions are anonymous, single-expression functions.

print("\n#B Lambda Expressions")

square = lambda x: x ** 2  # Lambda function for squaring a number
print("Square of 5:", square(5))

add = lambda x, y: x + y  # Lambda function for addition
print("Addition using lambda:", add(3, 7))

# Lambda in sorting
students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
students.sort(key=lambda student: student[1])  # Sort by age
print("Sorted students by age:", students)

#C Generators
# Generators produce values lazily using `yield`.

print("\n#C Generators")

def count_up_to(n):
    """Generator that counts from 1 to n."""
    count = 1
    while count <= n:
        yield count
        count += 1

counter = count_up_to(5)  # Create generator

print("Generated values:")
for num in counter:
    print(num)  # Prints numbers one by one

#D Attributes
# Attributes are variables associated with an object.

print("\n#D Attributes")

class Person:
    """A simple class with attributes."""
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

# Creating an object
p1 = Person("David", 35)

# Accessing attributes
print(f"Person Name: {p1.name}, Age: {p1.age}")

# Modifying attributes
p1.age = 36
print(f"Updated Age: {p1.age}")

# Adding a new attribute dynamically
p1.city = "New York"
print(f"City Attribute: {p1.city}")

# Checking if an attribute exists
print("Has attribute 'age'?", hasattr(p1, "age"))
print("Has attribute 'city'?", hasattr(p1, "city"))
