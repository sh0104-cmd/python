import numpy as np

# Original list
lst = [12.23, 13.32, 100, 36.32]
# Convert to 1D NumPy array
arr = np.array(lst)
print("Original List:", lst)
print("One-dimensional NumPy array:", arr)

# Create a 3x3 matrix with values from 2 to 10
matrix = np.arange(2, 11).reshape(3, 3)
print(matrix)

# Create a null vector of size 10
null_vec = np.zeros(10)
print("Original null vector:", null_vec)

# Update the sixth value to 11 (index 5)
null_vec[5] = 11
print("Updated vector:", null_vec)

# Create array with values from 12 to 38 (excluding 38)
arr_range = np.arange(12, 38)
print(arr_range)

# Original integer array
arr_int = np.array([1, 2, 3, 4])
# Convert to float
arr_float = arr_int.astype(float)
print("Original array:", arr_int)
print("Float type array:", arr_float)

# Celsius array
celsius = np.array([0, 12, 45.21, 34, 99.91, 0])
# Convert to Fahrenheit
fahrenheit = celsius * 9/5 + 32
print("Values in Centigrade degrees:", celsius)
print("Values in Fahrenheit degrees:", fahrenheit)

# Original array
orig_arr = np.array([10, 20, 30])
# Values to append
values_to_append = [40, 50, 60, 70, 80, 90]
# Append to array
appended_arr = np.append(orig_arr, values_to_append)
print("Original array:", orig_arr)
print("After append:", appended_arr)

# Random array of 10 elements
random_arr = np.random.rand(10)
# Compute stats
mean = np.mean(random_arr)
median = np.median(random_arr)
std_dev = np.std(random_arr)

print("Random array:", random_arr)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)

# 10x10 random array
rand_10x10 = np.random.rand(10, 10)
min_val = np.min(rand_10x10)
max_val = np.max(rand_10x10)

print("10x10 Random Array:\n", rand_10x10)
print("Minimum value:", min_val)
print("Maximum value:", max_val)

# 3x3x3 random array
rand_3x3x3 = np.random.rand(3, 3, 3)
print("3x3x3 Random Array:\n", rand_3x3x3)
