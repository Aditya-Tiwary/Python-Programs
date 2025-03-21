#A Units
# A unit in Python refers to a module, package, or built-in library that provides functionality.

print("#A Units")

# Python has built-in units (modules) that can be imported and used.

#B Import
# Import is used to bring external or built-in modules into the current script.

print("\n#B Import")

import math  # Importing the math module
print("Square root of 16:", math.sqrt(16))

#C from
# The 'from' statement allows importing specific parts of a module.

print("\n#C from")

from math import pi  # Importing only 'pi' from math module
print("Value of pi:", pi)

#D import*
# The 'import *' imports all public symbols from a module.

print("\n#D import*")

from math import *  # Importing all from math (not recommended)
print("Cosine of 0:", cos(0))  # Using cos() directly

#E Statements
# Python statements include assignments, conditionals, loops, and more.

print("\n#E Statements")

x = 10  # Assignment statement
if x > 5:  # Conditional statement
    print("x is greater than 5")  
for i in range(3):  # Loop statement
    print("Loop iteration:", i)

#F Python built-in Units sys
# The sys module provides system-related functions.

print("\n#F Python built-in Units sys")

import sys
print("Python Version:", sys.version)

#G copy
# The copy module allows copying objects.

print("\n#G copy")

import copy
original_list = [1, 2, [3, 4]]
copied_list = copy.deepcopy(original_list)
copied_list[2][0] = 99
print("Original List:", original_list)
print("Copied List:", copied_list)

#H Collections Unit
# The collections module provides specialized container datatypes.

print("\n#H Collections Unit")

from collections import Counter
counter = Counter("aabbbccddddd")
print("Character Frequency:", counter)

#I Functional Unit
# The functools module provides higher-order functions.

print("\n#I Functional Unit")

from functools import reduce
numbers = [1, 2, 3, 4]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum using reduce:", sum_of_numbers)

#J Bisect Unit
# The bisect module is used for maintaining a sorted list.

print("\n#J Bisect Unit")

import bisect
sorted_list = [1, 3, 4, 7]
bisect.insort(sorted_list, 5)  # Insert while maintaining order
print("Sorted List after insertion:", sorted_list)

#K Heapq Unit
# The heapq module provides a heap-based priority queue.

print("\n#K Heapq Unit")

import heapq
heap = [3, 1, 4, 1, 5]
heapq.heapify(heap)  # Convert list into a heap
heapq.heappush(heap, 2)  # Push new element
print("Smallest element:", heapq.heappop(heap))  # Remove smallest element

#L User Dict Unit
# The UserDict module allows creating dictionary-like objects.

print("\n#L User Dict Unit")

from collections import UserDict

class MyDict(UserDict):
    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError("Keys must be strings")
        super().__setitem__(key, value)

my_dict = MyDict()
my_dict["name"] = "Alice"
print("Custom Dict:", my_dict)

#M Optparse Unit
# The optparse module is used for command-line options parsing (deprecated, use argparse).

print("\n#M Optparse Unit")

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-n", "--name", dest="name", help="Enter your name")
(options, args) = parser.parse_args([])  # Normally, sys.argv would be passed
print("Optparse Example (if args were given):", options.name)

#N Itertools Unit
# The itertools module provides functions for working with iterators.

print("\n#N Itertools Unit")

import itertools
permutations = list(itertools.permutations([1, 2, 3]))
print("All permutations of [1,2,3]:", permutations)
