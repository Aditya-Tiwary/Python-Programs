#A Creating aFiles object with open
# The open() function is used to work with files in Python.

print("#A Creating aFiles object with open")

file_path = "example.txt"
with open(file_path, "w") as file:
    file.write("Hello, Python file handling!\nThis is a test file.")

print(f"File '{file_path}' has been created and written.")

#B Auxiliary Unit for File I/O
# Auxiliary modules like shutil and os help in file handling.

print("\n#B Auxiliary Unit for File I/O")

import shutil

shutil.copy(file_path, "copy_example.txt")  # Copying file
print(f"Copied '{file_path}' to 'copy_example.txt'")

#C The String IO and cString IO Units
# StringIO provides in-memory file-like objects.

print("\n#C The String IO and cString IO Units")

from io import StringIO

string_io = StringIO("This is an in-memory file.\nIt behaves like a real file.")
print("Reading from StringIO:")
print(string_io.read())

#D Text Input and Output
# Reading and writing plain text files.

print("\n#D Text Input and Output")

with open(file_path, "r") as file:
    content = file.read()

print("Content of the file:")
print(content)

#E Richer-Text I/O
# Using libraries like pandas for structured text data.

print("\n#E Richer-Text I/O")

import pandas as pd

data = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [25, 30]})
data.to_csv("data.csv", index=False)  # Writing data to a CSV file

df = pd.read_csv("data.csv")  # Reading from CSV
print("CSV File Content:")
print(df)

#F Interactive Command Sessions
# The `code` module allows interactive execution of Python code.

print("\n#F Interactive Command Sessions")

import code

# Starts an interactive session (disabled in script mode)
# code.interact(local=locals())

#G Internationalization
# The gettext module helps in language translations.

print("\n#G Internationalization")

import gettext

# Creating a translation function (normally, .mo files would be used)
gettext.translation("messages", localedir="locale", languages=["en"], fallback=True)
print(("Hello, world!"))  # Would be translated if locales are set up
