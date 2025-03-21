#A Try
# The try block is used to catch and handle exceptions.

print("#A Try")

try:
    result = 10 / 0  # This will cause a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    
#B Raise
# The raise statement is used to manually trigger an exception.

print("\n#B Raise")

try:
    age = -5
    if age < 0:
        raise ValueError("Age cannot be negative")  # Raising a ValueError
except ValueError as e:
    print("Exception caught:", e)

#C With Exceptions
# The 'with' statement is used for handling resources safely.

print("\n#C With Exceptions")

try:
    with open("example.txt", "w") as file:
        file.write("Hello, Python!")  # File is automatically closed after this block
    print("File written successfully.")
except IOError:
    print("An error occurred while handling the file.")

#D Exception Objects
# Exception objects contain error details and can be accessed inside the except block.

print("\n#D Exception Objects")

try:
    x = int("abc")  # This will cause a ValueError
except ValueError as e:
    print("Exception type:", type(e).__name__)  # Getting the exception type
    print("Exception message:", str(e))  # Printing exception message

#E Standard Exception Classes
# Python provides built-in exception classes like ValueError, TypeError, KeyError, etc.

print("\n#E Standard Exception Classes")

try:
    my_dict = {"name": "Alice"}
    print(my_dict["age"])  # This will cause a KeyError
except KeyError as e:
    print("Standard Exception caught:", e)

#F Custom Exception Classes
# We can define our own exception classes for specific error handling.

print("\n#F Custom Exception Classes")

class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    def __init__(self, value):
        self.value = value
        super().__init__(f"Negative numbers are not allowed: {value}")

try:
    num = -10
    if num < 0:
        raise NegativeNumberError(num)  # Raising custom exception
except NegativeNumberError as e:
    print("Custom Exception caught:", e)
