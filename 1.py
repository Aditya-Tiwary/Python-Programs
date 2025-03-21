#A Data types
# Python has several built-in data types including int, float, complex, str, list, tuple, set, and dict.

integer_value = 10  # Integer data type
float_value = 10.5  # Float data type
complex_value = 3 + 4j  # Complex number
string_value = "Hello, Python"  # String data type
list_value = [1, 2, 3, 4]  # List data type (mutable)
tuple_value = (1, 2, 3, 4)  # Tuple data type (immutable)
set_value = {1, 2, 3, 4}  # Set data type (unique elements)
dict_value = {"name": "Alice", "age": 25}  # Dictionary data type (key-value pairs)

print("Integer:", integer_value, type(integer_value))
print("Float:", float_value, type(float_value))
print("Complex:", complex_value, type(complex_value))
print("String:", string_value, type(string_value))
print("List:", list_value, type(list_value))
print("Tuple:", tuple_value, type(tuple_value))
print("Set:", set_value, type(set_value))
print("Dictionary:", dict_value, type(dict_value))

#B Variables and Other References
# Variables store references to objects in memory, and Python uses dynamic typing.

x = 10  # Variable x holds an integer
y = x  # y now references the same object as x
x = 20  # x now references a different object

print("\nVariable x:", x)  # Outputs 20
print("Variable y:", y)  # Outputs 10 (since integers are immutable)

# Mutable object reference example
list1 = [1, 2, 3]
list2 = list1  # Both list1 and list2 point to the same object

list1.append(4)
print("List1:", list1)  # Outputs [1, 2, 3, 4]
print("List2:", list2)  # Outputs [1, 2, 3, 4] (changes reflect in both)

#C Expression and Operators
# Expressions consist of variables, operators, and function calls that evaluate to a value.

a = 10
b = 5

# Arithmetic Operators
add = a + b  # Addition
sub = a - b  # Subtraction
mul = a * b  # Multiplication
div = a / b  # Division
mod = a % b  # Modulus
exp = a ** b  # Exponentiation
floor_div = a // b  # Floor division

print("\nAddition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)
print("Modulus:", mod)
print("Exponentiation:", exp)
print("Floor Division:", floor_div)

# Comparison Operators
print("\nComparison Operators:")
print(a == b)  # Equal to
print(a != b)  # Not equal to
print(a > b)   # Greater than
print(a < b)   # Less than
print(a >= b)  # Greater than or equal to
print(a <= b)  # Less than or equal to

# Logical Operators
print("\nLogical Operators:")
print(a > 5 and b < 10)  # Logical AND
print(a > 5 or b > 10)  # Logical OR
print(not(a > 5))  # Logical NOT

# Bitwise Operators
print("\nBitwise Operators:")
print(a & b)  # AND
print(a | b)  # OR
print(a ^ b)  # XOR
print(~a)  # NOT
print(a << 1)  # Left shift
print(a >> 1)  # Right shift
