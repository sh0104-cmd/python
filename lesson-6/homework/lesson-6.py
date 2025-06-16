#1.Modify String with Underscores
def insert_underscores(txt):
    vowels = 'aeiouAEIOU'
    result = []
    i = 0
    count = 0

    while i < len(txt):
        result.append(txt[i])
        count += 1

        if count == 3:
            # Check if current character is vowel or followed by underscore
            if txt[i] in vowels or (i + 1 < len(txt) and txt[i + 1] == '_'):
                # Shift underscore to next character if possible
                if i + 1 < len(txt) - 1:
                    result.append(txt[i + 1])
                    result.append('_')
                    i += 1  # Skip the shifted character
                # If there's no room to insert, skip underscore
            else:
                if i + 1 < len(txt):  # Avoid adding underscore at end
                    result.append('_')
            count = 0  # Reset count after every 3 characters (with or without underscore)
        i += 1

    return ''.join(result)
print(insert_underscores("abcdefghijk"))      # Output: "abc_def_ghi_jk"
print(insert_underscores("abcdeiouxyz"))      # Output: "abc_dei_oux_yz"
print(insert_underscores("aeiobcdufgh"))      # Output: "aei_obc_duf_gh"

#2.
n=int(input("enter integer:"))
for i in range(n):
    print(i**2)

#3.Loop-Based Exercises
#Exercise 1: Print first 10 natural numbers using a while loop

i=1
while i<=10:
    print(i)
    i+=1

#2.Exercise 2: Print the following pattern
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=' ')
    print()

#Exercise 3: Calculate sum of all numbers from 1 to a given number
# Input: the number up to which to sum
n = int(input("Enter a number: "))

# Initialize sum
total = 0

# Loop through 1 to n
for i in range(1, n + 1):
    print(f"Add {i} → {total} + {i}")
    total += i

# Final result (optional)
print(f"Total sum = {total}")

#Exercise 4: Print multiplication table of a given number
n=int(input("enter number:"))
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")
    i+=1

#Exercise 5: Display numbers from a list using a loop
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break
    if num % 5 == 0 and num >= 75:
        print(num)

#Exercise 6: Count the total number of digits in a number

number=75869
print(len(str(number)))


#Exercise 7: Print reverse number pattern
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()

#Exercise 8: Print list in reverse order using a loop
#Given:

list1 = [10, 20, 30, 40, 50]
for i in list1[::-1]:
    print(i)

#Exercise 9: Display numbers from -10 to -1 using a for loop
for i in range(-10,0):
    print(i)

#Exercise 10: Display message “Done” after successful loop execution

for i in range(0,5):
    print(i)
print('Done!')

#Exercise 11: Print all prime numbers within a range
start = 25
end = 50

print(f"Prime numbers between {start} and {end}:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)

#Exercise 12: Display Fibonacci series up to 10 terms
# Example:

# Fibonacci sequence:
# 0  1  1  2  3  5  8  13  21  34

n_terms = 10
n1, n2 = 0, 1
count = 0

print("Fibonacci sequence:")

while count < n_terms:
    print(n1, end="  ")
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1

# #Exercise 13: Find the factorial of a given number
# Example:

# 5! = 120

num = 5
factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("0! = 1")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"{num}! = {factorial}")

#4. Return Uncommon Elements of Lists
# Task
# Return the elements that are not common between two lists. The order of elements does not matter.

# Examples
# Input: list1 = [1, 1, 2], list2 = [2, 3, 4]
# Output: [1, 1, 3, 4]

# Input: list1 = [1, 2, 3], list2 = [4, 5, 6]
# Output: [1, 2, 3, 4, 5, 6]

# Input: list1 = [1, 1, 2, 3, 4, 2], list2 = [1, 3, 4, 5]
# Output: [2, 2, 5]
from collections import Counter

def not_common_elements(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    
    # Subtract counters in both directions
    diff1 = c1 - c2
    diff2 = c2 - c1
    
    # Combine the remaining items
    result = list(diff1.elements()) + list(diff2.elements())
    
    return result

print(not_common_elements([1, 1, 2], [2, 3, 4]))      
# Output: [1, 1, 3, 4]

print(not_common_elements([1, 2, 3], [4, 5, 6]))      
# Output: [1, 2, 3, 4, 5, 6]

print(not_common_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  
# Output: [1, 2, 2, 5]
