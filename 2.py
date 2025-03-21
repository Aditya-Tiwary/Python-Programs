#A Numeric Operations
# Python supports various numeric operations on integers, floats, and complex numbers.

a = 15
b = 4

# Basic arithmetic operations
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b  # Floating point division
floor_division = a // b  # Integer division
modulus = a % b  # Remainder
exponentiation = a ** b  # Power

print("#A Numeric Operations")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Floor Division:", floor_division)
print("Modulus:", modulus)
print("Exponentiation:", exponentiation)

#B Sequence Operations
# Sequences in Python include lists, tuples, and strings. They support indexing, slicing, and concatenation.

seq1 = [1, 2, 3, 4, 5]
seq2 = (10, 20, 30, 40)
seq3 = "Python"

print("\n#B Sequence Operations")
print("First element of list:", seq1[0])  # Indexing
print("Slice of tuple:", seq2[1:3])  # Slicing
print("Concatenation:", seq1 + [6, 7])  # Concatenation
print("Repetition:", seq3 * 2)  # Repeating sequences

#C Strings
# Strings are immutable sequences of characters.

str1 = "Hello, Python!"

print("\n#C Strings")
print("Length of string:", len(str1))
print("Uppercase:", str1.upper())
print("Lowercase:", str1.lower())
print("Replace 'Python' with 'World':", str1.replace("Python", "World"))
print("Splitting:", str1.split(","))
print("Checking if alphabetic:", str1.isalpha())

#D Tuples
# Tuples are immutable ordered collections.

tuple1 = (1, 2, 3, 4, 5)

print("\n#D Tuples")
print("Tuple:", tuple1)
print("First element:", tuple1[0])
print("Slicing:", tuple1[1:4])
print("Tuple length:", len(tuple1))

#E List
# Lists are mutable ordered collections.

list1 = [10, 20, 30, 40]

print("\n#E List")
list1.append(50)  # Adding an element
print("List after append:", list1)
list1.insert(2, 25)  # Inserting at index
print("List after insert:", list1)
list1.pop()  # Removing last element
print("List after pop:", list1)
list1.remove(20)  # Removing a specific value
print("List after remove:", list1)

#F Set Operations
# Sets are unordered collections of unique elements.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("\n#F Set Operations")
print("Union:", set1 | set2)  # Union
print("Intersection:", set1 & set2)  # Intersection
print("Difference:", set1 - set2)  # Difference
print("Symmetric Difference:", set1 ^ set2)  # Elements in either set but not both

#G Dictionary Operations
# Dictionaries store key-value pairs.

dict1 = {"name": "Alice", "age": 25, "city": "New York"}

print("\n#G Dictionary Operations")
print("Dictionary:", dict1)
print("Accessing 'name':", dict1["name"])
dict1["age"] = 26  # Modifying a value
print("Updated dictionary:", dict1)
dict1["country"] = "USA"  # Adding a new key-value pair
print("After adding 'country':", dict1)
del dict1["city"]  # Removing a key
print("After deleting 'city':", dict1)
