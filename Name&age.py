# Create a program that asks the user to enter their name and their age
#Print out a message that will tell them the year that they will turn 95 years old.

#!/usr/bin/python3

import datetime
name=input("Enter your name: ")
age =int(input("Enter your age: "))
z=95-age
x=datetime.datetime.now()
y=(x.year)
p=y+z
print(name)
print(age)
print("Year, when your age will be 95: " , p)
