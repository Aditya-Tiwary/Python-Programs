#A Methods of String Objects
def string_methods_demo():
    text = "Hello World"
    # Common string methods
    print(text.lower())          # Convert to lowercase
    print(text.upper())          # Convert to uppercase
    print(text.capitalize())     # Capitalize first letter
    print(text.replace("World", "Python"))  # Replace substring
    print(text.split())         # Split into list
    print(text.strip())         # Remove leading/trailing whitespace
    print(text.find("World"))   # Find substring position

#B String Unit
def string_properties():
    message = "Python Programming"
    # Basic string operations
    print(len(message))         # Get string length
    print(message[0])          # Access first character
    print(message[-1])         # Access last character
    print(message[0:6])        # Slicing
    print("Python" in message) # Check if substring exists

#C String Formatting
def string_formatting_demo():
    name = "Alice"
    age = 25
    # Different formatting methods
    print("My name is %s and I'm %d" % (name, age))  # Old style
    print("My name is {} and I'm {}".format(name, age))  # Format method
    print(f"My name is {name} and I'm {age}")  # f-strings (Python 3.6+)

#D Pprint Unit
from pprint import pprint
def pprint_demo():
    data = {
        "name": "John",
        "hobbies": ["reading", "gaming", "coding"],
        "details": {"age": 30, "city": "New York"}
    }
    # Pretty print complex data structure
    pprint(data, indent=2)

#E Repr Unit
def repr_demo():
    class Person:
        def __init__(self, name):
            self.name = name
        
        def __repr__(self):
            return f"Person(name='{self.name}')"
    
    p = Person("Bob")
    print(repr(p))  # Shows object representation
    print(str(p))   # Shows string conversion

#F Unicode
def unicode_demo():
    # Working with Unicode characters
    text = "Hello 世界"  # Mixing English and Chinese
    print(text)
    print(text.encode("utf-8"))  # Encode to bytes
    print("\u2665")             # Unicode heart symbol
    print(ord("A"))            # Get Unicode code point
    print(chr(65))            # Get character from code point

#G Regular Expressions and the Re Units
import re
def regex_demo():
    text = "Contact: john@example.com or 123-456-7890"
    # Common regex patterns
    email_pattern = r"[\w\.-]+@[\w\.-]+"
    phone_pattern = r"\d{3}-\d{3}-\d{4}"
    
    # Find matches
    email = re.search(email_pattern, text)
    phone = re.search(phone_pattern, text)
    
    print(f"Email found: {email.group()}")
    print(f"Phone found: {phone.group()}")
    
    # Replace pattern
    new_text = re.sub(email_pattern, "REDACTED", text)
    print(new_text)

# Main execution
if __name__ == "__main__":
    print("#A String Methods Demo")
    string_methods_demo()
    print("\n#B String Properties")
    string_properties()
    print("\n#C String Formatting")
    string_formatting_demo()
    print("\n#D Pprint Demo")
    pprint_demo()
    print("\n#E Repr Demo")
    repr_demo()
    print("\n#F Unicode Demo")
    unicode_demo()
    print("\n#G Regular Expressions Demo")
    regex_demo()