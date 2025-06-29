#Create a list containing five different fruits and print the third fruit.
my_list=['apple','pear','mango','banana','ananas']
print(my_list[2])

#Create two lists of numbers and concatenate them into a single list.
num1=[1,2,3]
num2=[4,5,6]
single_list=num1+num2
single_list

numbers = [10, 20, 30, 40, 50, 60, 70]

first = numbers[0]
middle = numbers[len(numbers) // 2]
last = numbers[-1]

result = [first, middle, last]
print(result)  # Output: [10, 40, 70]

#Convert List to Tuple
#Create a list of your five favorite movies and convert it into a tuple.
my_list=['saw','purge','parasyte','deaths game','forgotten']
my_tuple=tuple(my_list)
my_tuple

#Check Element in a List
#Given a list of cities, check if "Paris" is in the list and print the result.
city=['Tashkent','London','Paris']
print('Paris' in city)
if "Paris" in city:
    print("✅ Paris is in the list.")
else:
    print("❌ Paris is not in the list.")

#Duplicate a List Without Using Loops. Create a list of numbers and duplicate it without using loops.
original = [1, 2, 3, 4, 5]
duplicate = original * 2  # Duplicates the list
print(duplicate)

#Swap First and Last Elements of a List
Given a list of numbers, swap the first and last elements.
numbers = [10, 20, 30, 40, 50]

# Swap first and last
numbers[0], numbers[-1] = numbers[-1], numbers[0]

print("After swapping:", numbers)

#Slice a Tuple
#Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
# Create a tuple of numbers from 1 to 10
numbers = tuple(range(1, 11))  # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Slice from index 3 to 7 (index 3 to 6, since end is exclusive)
slice_result = numbers[3:7]

print("Original Tuple:", numbers)
print("Sliced Tuple (index 3 to 6):", slice_result)

#Count Occurrences in a List
#Create a list of colors and count how many times "blue" appears in the list.

colors = ["red", "blue", "green", "blue", "yellow", "blue"]

blue_count = colors.count("blue")

print(f'"blue" appears {blue_count} times.')

#Find the Index of an Element in a Tuple
#Given a tuple of animals, find the index of "lion".

animals = ("cat", "dog", "lion", "tiger", "elephant")

index_of_lion = animals.index("lion")

print(f"The index of 'lion' is: {index_of_lion}")

#Merge Two Tuples
#Create two tuples of numbers and merge them into a single tuple.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

merged_tuple = tuple1 + tuple2

print("Merged Tuple:", merged_tuple)

#Find the Length of a List and Tuple
#Given a list and a tuple, find and print their lengths.

my_list = [10, 20, 30, 40, 50]
my_tuple = ('a', 'b', 'c', 'd')

list_length = len(my_list)
tuple_length = len(my_tuple)

print("Length of the list:", list_length)
print("Length of the tuple:", tuple_length)

# Create a tuple of five numbers
numbers_tuple = (10, 20, 30, 40, 50)

# Convert the tuple to a list
numbers_list = list(numbers_tuple)

print("Original Tuple:", numbers_tuple)
print("Converted List:", numbers_list)

#Find Maximum and Minimum in a Tuple
Given a tuple of numbers, find and print the maximum and minimum values.
numbers = (15, 22, 8, 19, 31, 4)

maximum = max(numbers)
minimum = min(numbers)

print("Maximum value:", maximum)
print("Minimum value:", minimum)

#Reverse a Tuple
#Create a tuple of words and print it in reverse order.
words = ("apple", "banana", "cherry", "date")

# Method 1: Using slicing
reversed_tuple = words[::-1]

# Method 2 (alternative): Using reversed() and tuple()
#reversed_tuple = tuple(reversed(words))
#print(reversed_tuple)
print("Original Tuple:", words)
print("Reversed Tuple:", reversed_tuple)




