#A The print
# The print function is used to display output in Python.

print("#A The print")
print("Hello, World!")  # Printing a simple message
name = "Alice"
age = 25
print("Name:", name, "Age:", age)  # Printing multiple values
print(f"Formatted String: My name is {name} and I am {age} years old.")  # f-string formatting
print("This is a", "concatenated", "message.", sep="-")  # Using separator

#B Control Flow Statements
# if-elif-else is used for decision-making.

print("\n#B Control Flow Statements")
x = 10
if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")

#C while
# The while loop repeats code while a condition is true.

print("\n#C while")
count = 0
while count < 5:
    print("Count:", count)
    count += 1  # Increment

#D for
# The for loop is used to iterate over sequences.

print("\n#D for")
for i in range(5):  # Loop from 0 to 4
    print("Iteration:", i)

#E break
# The break statement exits a loop immediately.

print("\n#E break")
for i in range(5):
    if i == 3:
        break  # Stops the loop when i is 3
    print("Number:", i)

#F continue for
# The continue statement skips the current iteration and moves to the next one.

print("\n#F continue for")
for i in range(5):
    if i == 2:
        continue  # Skips when i is 2
    print("Number:", i)

#G pass
# The pass statement is used as a placeholder for future code.

print("\n#G pass")
for i in range(3):
    if i == 1:
        pass  # Placeholder, does nothing
    else:
        print("Number:", i)

#H try
# The try block is used to handle exceptions.

print("\n#H try")
try:
    result = 10 / 0  # This will cause a division by zero error
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

#I raise
# The raise statement is used to trigger an exception manually.

print("\n#I raise")
try:
    age = -5
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print("Exception caught:", e)

#J with
# The with statement is used for resource management, such as handling files.

print("\n#J with")
with open("example.txt", "w") as file:
    file.write("Hello, Python!")  # Automatically closes the file after use

print("File written successfully.")
