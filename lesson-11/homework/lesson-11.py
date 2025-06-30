#Create your own virtual environment and install some python packages.
python -m venv myenv
myenv\Scripts\activate
pip install requests numpy


#Create custom modules.
# Create math_operations.py module. Define add, subtract, multiply and divide functions in it. (All functions accept two arguments in this task)
# Create string_utils.py module. Define reverse_string and count_vowels functions in it. (All functions accept one argument in this task)
# Create custom packages.
# Create geometry package.
#  geometry\
#      __init__.py
#      circle.py

# math_operations.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"


# string_utils.py

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    return sum(1 for char in s.lower() if char in "aeiou")





# Define calculate_area and calculate_circumference functions in circle.py. These functions accept one argument(radius).
# Create file_operations package.
#  file_operations\
#      __init__.py
#      file_reader.py
#      file_writer.py

geometry/
├── __init__.py
└── circle.py

# geometry/circle.py

import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius

# Define read_file function in file_reader.py. This function accepts one argument(file_path). Define write_file function in file_writer.py. This function accepts two arguments(file_path, content).

file_operations/
├── __init__.py
├── file_reader.py
└── file_writer.py

# file_operations/file_reader.py

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# file_operations/file_writer.py

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
from math_operations import add, subtract
from string_utils import reverse_string, count_vowels
from geometry.circle import calculate_area, calculate_circumference
from file_operations.file_writer import write_file
from file_operations.file_reader import read_file

# Math operations
print(add(10, 5))
print(subtract(10, 5))

# String utilities
print(reverse_string("hello"))
print(count_vowels("OpenAI"))

# Geometry
print(calculate_area(5))
print(calculate_circumference(5))

# File operations
write_file("sample.txt", "Hello from custom package!")
print(read_file("sample.txt"))

 
