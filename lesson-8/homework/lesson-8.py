try:
    num = int(input("Enter a number: "))
    result = num / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

try:
    user_input = input("Enter an integer: ")
    number = int(user_input)
except ValueError:
    print("Error: That's not a valid integer.")
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found.")

try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    if not a.isdigit() or not b.isdigit():
        raise TypeError("Inputs must be numerical.")
    result = int(a) + int(b)
    print("Sum:", result)
except TypeError as e:
    print("Error:", e)

try:
    with open("/root/secret.txt", "r") as file:
        content = file.read()
except PermissionError:
    print("Error: Permission denied to read the file.")

try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("Error: List index out of range.")

try:
    num = input("Enter a number (press Ctrl+C to cancel): ")
    print("You entered:", num)
except KeyboardInterrupt:
    print("\nInput cancelled by user.")
try:
    a = 10
    b = 0
    result = a / b  # triggers ZeroDivisionError, subclass of ArithmeticError
except ArithmeticError:
    print("Error: An arithmetic error occurred.")

try:
    with open("file_with_encoding_issue.txt", "r", encoding="ascii") as file:
        content = file.read()
except UnicodeDecodeError:
    print("Error: Cannot decode file content due to encoding issues.")

try:
    my_list = [1, 2, 3]
    my_list.upper()  # list has no attribute 'upper'
except AttributeError:
    print("Error: List object has no such attribute.")
  #Python File Input Output: Exercises, Practice, Solution
#1.
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
#2. Read first n lines of a file

n = 3
with open("example.txt", "r") as file:
    for i in range(n):
        print(file.readline(), end="")
#3. Append text to a file and display the text

with open("example.txt", "a") as file:
    file.write("\nAppended line.")

with open("example.txt", "r") as file:
    print(file.read())
#4. Read last n lines of a file

n = 3
with open("example.txt", "r") as file:
    lines = file.readlines()
    print("".join(lines[-n:]))
#5. Read a file line by line into a list

with open("example.txt", "r") as file:
    lines = file.readlines()
print(lines)
#6. Read a file line by line into a variable

with open("example.txt", "r") as file:
    content = ""
    for line in file:
        content += line
print(content)
#7. Read a file line by line into an array

with open("example.txt", "r") as file:
    array = [line.strip() for line in file]
print(array)
#8. Find the longest words

with open("example.txt", "r") as file:
    words = file.read().split()
    longest = max(words, key=len)
print("Longest word:", longest)
#9. Count the number of lines in a file

with open("example.txt", "r") as file:
    line_count = sum(1 for _ in file)
print("Number of lines:", line_count)
#10. Count word frequency in a file

from collections import Counter

with open("example.txt", "r") as file:
    words = file.read().replace(',', ' ').split()
    freq = Counter(words)
print(freq)
#11. Get the file size (in bytes)

import os

file_size = os.path.getsize("example.txt")
print("File size:", file_size, "bytes")
#12. Write a list to a file

lines = ['Line 1', 'Line 2', 'Line 3']
with open("list_output.txt", "w") as file:
    for item in lines:
        file.write(item + "\n")
#13. Copy contents of one file to another

with open("example.txt", "r") as src, open("copy.txt", "w") as dest:
    dest.write(src.read())
#14. Combine lines from two files

with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    for line1, line2 in zip(f1, f2):
        print(line1.strip() + " " + line2.strip())
#15. Read a random line from a file

import random

with open("example.txt", "r") as file:
    lines = file.readlines()
    print(random.choice(lines).strip())
#16. Check if a file is closed

file = open("example.txt", "r")
print("Is file closed?", file.closed)
file.close()
print("Is file closed now?", file.closed)
#17. Remove newline characters from a file

with open("example.txt", "r") as file:
    lines = [line.strip() for line in file]
print(lines)
#18. Count words in a file (handles commas)

with open("example.txt", "r") as file:
    content = file.read().replace(',', ' ')
    words = content.split()
    print("Number of words:", len(words))
#19. Extract characters from files into a list

import glob

char_list = []
for filename in glob.glob("*.txt"):
    with open(filename, "r") as file:
        char_list.extend(list(file.read()))
print(char_list)
#20. Generate 26 text files (A.txt to Z.txt)


import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as file:
        file.write(f"This is {letter}.txt")
#21. Create file with alphabet letters, n per line


import string

n = 5  # letters per line
letters = string.ascii_lowercase

with open("alphabet.txt", "w") as file:
    for i in range(0, len(letters), n):
        file.write("".join(letters[i:i+n]) + "\n")
