#1.def is_leap(year): """ Determines whether a given year is a leap year.

def is_leap_year(year):
    """
    Determine whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.

    Parameters:
    year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(is_leap_year(2020))  # True
print(is_leap_year(1900))  # False
print(is_leap_year(2000))  # True


#2. Conditional Statements Exercise
#Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

def check_weirdness(n):
    if n % 2 == 1:  # Check if n is odd
        print("Weird")
    elif n % 2 == 0:  # Check if n is even
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")

# Example usage:
n = int(input("Enter an integer: "))
check_weirdness(n)


# #3.Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.
# Give two solutions.

# Solution 1 with if-else statement.

# Solution 2 without if-else statement.
def even_numbers_inclusive_if_else(a, b):
    if a > b:
        return list(range(a + (a % 2), b - 1, -2)) if a % 2 == 0 else list(range(a - 1, b - 1, -2))
    else:
        return list(range(a + (a % 2), b + 1, 2))
print(even_numbers_inclusive_if_else(3, 10))  # Output: [4, 6, 8, 10]
print(even_numbers_inclusive_if_else(10, 3))  # Output: [10, 8, 6, 4]

def even_numbers_inclusive_no_if(a, b):
    start = a + (a % 2)
    end = b + 1
    return list(range(start, end, 2)) if a <= b else list(range(start, b - 1, -2))
print(even_numbers_inclusive_no_if(3, 10))  # Output: [4, 6, 8, 10]
print(even_numbers_inclusive_no_if(10, 3))  # Output: [10, 8, 6, 4]

