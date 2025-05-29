#1.Given a side of square. Find its perimeter and area.
s=int(input('Side:'))
P=4*s
A=s**2
print(P,A)

#2.Given diameter of circle. Find its length.
import math
d=int(input('Diameter:'))
length=math.pi*d
print(length)

#3.Given two numbers a and b. Find their mean.
a=int(input('a:'))
b=int(input('b:'))
mean=(a+b)/2
print(mean)

#4.Given two numbers a and b. Find their sum, product and square of each number.
a=int(input('a:'))
b=int(input('b:'))
sum=a+b
product=a*b
square_a=a**2
square_b=b**2
print(sum,product,square_a,square_b)
