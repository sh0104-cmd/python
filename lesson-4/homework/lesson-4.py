#Dictionary Exercises
#1. Sort a Dictionary by Value
#Write a Python script to sort (ascending and descending) a dictionary by value.
# Sample dictionary
sample_dict = {
    'apple': 10,
    'banana': 5,
    'cherry': 15,
    'date': 7
}

# Sort dictionary by value in ascending order
ascending_sorted = dict(sorted(sample_dict.items(), key=lambda item: item[1]))

# Sort dictionary by value in descending order
descending_sorted = dict(sorted(sample_dict.items(), key=lambda item: item[1], reverse=True))

# Display the results
print("Original Dictionary:")
print(sample_dict)

print("\nSorted Dictionary (Ascending by Value):")
print(ascending_sorted)

print("\nSorted Dictionary (Descending by Value):")
print(descending_sorted)

#2. Add a Key to a Dictionary
#Write a Python script to add a key to a dictionary.
numbers={0: 10, 1: 20}
numbers[2]=30
print(numbers)

#3.Concatenate Multiple Dictionaries
#Write a Python script to concatenate the following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)

#4.Generate a Dictionary with Squares
#Write a Python script to generate and 
#print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
res = {}
for i in range(1,6):
    res[i] = i**2
print(res)


#5.Dictionary of Squares (1 to 15)
#Write a Python script to print a dictionary where the keys are numbers 
#between 1 and 15 (both included) and the values are the square of the keys.

res = {}
for i in range(1,16):
    res[i] = i**2
print(res)

#Set Exercises
#1. Create a Set
#Write a Python program to create a set.

# Creating a set in Python
my_set = {1, 2, 3, 4, 5}

# Display the set
print("The set is:", my_set)

#2.Iterate Over a Set
#Write a Python program to iterate over sets.
# Define a set
fruits = {"apple", "banana", "cherry", "mango"}
# Iterate over the set
print("Iterating over the set:")
for fruit in fruits:
    print(fruit)

#3.Add Member(s) to a Set
#Write a Python program to add member(s) to a set.
fruits.add("pear")
print(fruits)

#4.Remove Item(s) from a Set
#Write a Python program to remove item(s) from a given set.
fruits.remove("banana")
print(fruits)

#5.Remove an Item if Present in the Set
#Write a Python program to remove an item from a set if it is present in the set.
# Define a set
fruits = {"apple", "banana", "cherry", "mango"}

# Item to remove
item_to_remove = "banana"

# Check if the item is in the set, then remove it
if item_to_remove in fruits:
    fruits.remove(item_to_remove)
    print(f"{item_to_remove} has been removed.")
else:
    print(f"{item_to_remove} not found in the set.")

# Print the updated set
print("Updated set:", fruits)
