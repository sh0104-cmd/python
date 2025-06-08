#1.Age Calculator
#Write a Python program to ask for a user's name and year of birth, then calculate and display their age.
user_name=input('Enter your name:')
year_of_birth=int(input("Enter your birth year:"))
import datetime
current_year=datetime.datetime.today()
print(user_name) #name of a user
print(current_year.year-year_of_birth) # age of a user


#2.Extract Car Names
#Extract car names from the following text:
txt = 'LMaasleitbtui'
print(txt[::2])
print(txt[1::2])

#3.Extract Car Names
#Extract car names from the following text:
txt = 'MsaatmiazD'
print(txt[::2])
print(txt[-1::-2])

#4.Extract Residence Area
#Extract the residence area from the following text:
txt = "I'am John. I am from London"
txt2=txt.split(' ')
print(txt2[-1])

#5.Reverse String
#Write a Python program that takes a user input string and prints it in reverse order.
user=input('Enter your name:')
print(user[::-1])

#6.Count Vowels
#Write a Python program that counts the number of vowels in a given string.

name=input('Enter name:')
vowels="aoeiu"
cnt=0
for char in name:
 if char in vowels:
    cnt=cnt+1
    print('Number of vowels: ',cnt)

    #7.Find Maximum Value
#Write a Python program that takes a list of numbers as input and prints the maximum value.
numbers=list(input('Enter numbers:'))
print('max number:', max(numbers))

#8. Check Palindrome
#Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
name=input('Enter name:')
if name==name[::-1]:
    print (True)
else:
    print(False)

    #9.Extract Email Domain
#Write a Python program that extracts and prints the domain from an email address provided by the user.

email=input('Enter email:')
domain=email.split('@')
print('Domain:', domain[1])

#10.Generate Random Password
#Write a Python program to generate a random password containing letters, digits, and special characters.
import random
import string

# Combine all characters: letters + digits + special characters
characters = string.ascii_letters + string.digits + string.punctuation

# Set desired password length
length = 10  # you can change this number

# Generate random password
password = ''.join(random.choice(characters) for _ in range(length))

print("Generated password:", password)
