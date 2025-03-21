#A Classes and Instances
# A class is a blueprint for creating objects, and an instance is a specific object created from that class.

print("#A Classes and Instances")

class Person:
    """Class representing a person."""
    
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable
    
    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Creating an instance of the Person class
person1 = Person("Alice", 30)
print(person1.introduce())

#B Bound and Unbound Methods
# Bound methods are associated with an instance, while unbound methods are accessed from the class.

print("\n#B Bound and Unbound Methods")

class Sample:
    def instance_method(self):
        return "This is a bound method."

# Creating an instance
obj = Sample()
print(obj.instance_method())  # Bound method (called via instance)

# Unbound method (in Python 3, methods are automatically bound when accessed via an instance)
print(Sample.instance_method(obj))  # Explicitly passing an instance

#C Overriding
# Overriding occurs when a subclass provides a specific implementation of a method from its superclass.

print("\n#C Overriding")

class Animal:
    def speak(self):
        return "Animal makes a sound."

class Dog(Animal):
    def speak(self):
        return "Dog barks."

dog = Dog()
print(dog.speak())  # Overridden method

#D Superclass Methods
# The `super()` function is used to call methods from the superclass.

print("\n#D Superclass Methods")

class Vehicle:
    def describe(self):
        return "This is a vehicle."

class Car(Vehicle):
    def describe(self):
        return super().describe() + " It has four wheels."

car = Car()
print(car.describe())  # Calls superclass method and extends it

#E Decorators
# Decorators modify the behavior of functions or methods.

print("\n#E Decorators")

def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def greet():
    return "hello, world!"

print(greet())  # Output in uppercase due to decorator

#F Metaclasses
# Metaclasses define the behavior of class creation itself.

print("\n#F Metaclasses")

class Meta(type):
    """Custom metaclass that modifies class creation."""
    def __new__(cls, name, bases, class_dict):
        class_dict["greeting"] = "Hello from Metaclass!"
        return super().__new__(cls, name, bases, class_dict)

class MyClass(metaclass=Meta):
    pass

# Accessing the dynamically added attribute from metaclass
print(MyClass.greeting)  # "Hello from Metaclass!"
