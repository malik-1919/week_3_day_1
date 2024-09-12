# # Review
 # create variables for the following :
 # 1. age
age= 17 #integer variable 
 # 2. name
name= "Malik" #string variable 
 # 3. song
song=" Pride" #string variable 
 # 4. food
food= "pizza" #string variable 
 # 5. number
number= 30 #integer variable 
 

 # #now include the variables you just made print in the following...
# Once upon a time, there was a [age] old coder named [name].
#concatenation--- + around your variables
print("once upon a time there was a" +str (age) + "year old coder named" + name + ",")
print("there was a number" +str (number)+"as well")
#put the age and number in a new sentence 
print("The age" +str(age)+ "and the number" +str(number)+ "are numbers") 
# [name] liked to hum the song [song] while coding. It was so annoying that their teammates would throw [food] until [name] would stop singing.
date_of_birth=2021
Number2=123
number3=123.456
number4=123.33
number5=4555
#create a sentence of all this above
print("date of birth is"+ str(date_of_birth)+"and they are somehow"+str(Number2) +"," +str(number3) +","+str(number4)+","+str (number5)+"years old")
print(f"date of birth of is {date_of_birth} and is {number3} and the other person is {number4}")
# Still, [name] was the best coder on the team and could write [number] lines of code every day. Maybe [song] was [name]’s secret power?
##########################################################################################


















##########################################################################################
# The names you use when creating these labels need to follow a few rules:
# 1. Names can not start with a number.
# 2. There can be no spaces in the name, use _ instead.
# 3. Can't use any of these symbols :'",<>/?|\()!@#$%^&*~-+
# 4. It's considered best practice (PEP8) that names are lowercase.
# 5. Avoid using the characters 'l' (lowercase letter el), 'O' (uppercase letter oh),
#    or 'I' (uppercase letter eye) as single character variable names.
# 6. Avoid using words that have special meaning in Python like "list" and "str"


# Here are some exercises to practice the rules:


# Correcting Invalid Names: Below are some invalid names. Correct them according to the rules:


# first_name
# last_name
# emailaddress
# percent
# variablename
# zero
# list # this is a keyword in python 
#you cannot use it for your own variable name
# Creating Valid Names: Create valid names for the following descriptions:


# The first name of a person
# The last name of a person
# The email address of a person
# The percentage of marks obtained by a student
# A variable to store the number of items in a shopping cart




# Identify Valid and Invalid Names: Identify which of the following names are valid or invalid according to the rules:


# first_name
# lastName
# email_address
# percentage
# variable_name
# one_variable
# email_address
# percentage
# internet 
















############################################################################################


# # **Working with** **numbers** **bold text**
# We'll learn about the following topics:
# 1. Types of Numbers in Python
# 2. Basic Arithmetic
# 3. Differences between classic division and floor division


# Python has various "types" of numbers (numeric literals).
# 1. We'll mainly focus on integers and floating point numbers.
# Integers are just whole numbers, positive or negative. For example: 2 and -2 are examples of integers.
# 2. Floating point numbers in Python are notable because they have a decimal point in them, or use an exponential (e) to define the number. For example 2.0 and -2.1 are examples of floating point numbers. 4E2 (4 times 10 to the power of 2) is also an example of a floating point number in Python.


##########################################################################################
# #addition
print(2+1)
# #multiplication
print(2*2)
# #division
print(6/2)
# #modulo
print(7%4) # a remainder of 7 divided by 4
# #powers
print(2**3) #2 to the power of 3
# #get the max and min of a number
print("the max of 2 and 3 is",max(2,3))
#max means the highest number
print("the min of 2 and 3 is",min(2,3))
#min means the lowest number


# #round a number
print("round 3.9 is",round(3.9))
# # absolute value 
print("the absolute value of -3 is",abs(-3))
#absolute value means the distance from 0
# it will always be postive 
# # absolute value
# # order of operations
print("2 + 10 * 10 + 3 is",2 + 10 * 10 + 3)
# order of operations is the same as in math
# it means do the multiplication first
# then do the addition 


# #to do more you need to import special math libraries from python
from math import * 
# this goes out and grabs some different math functions we can use
# # floor method 
print("the floor of 3.7 is",floor(3.7))
#floor means round down
# cell method 
print("the ceil of 3.7 is",ceil(3.7))
print("the ceil of 6.6 is",ceil(6.6))
# ceil means round up
# # sqrt method 

# #from math import *    
# #this goes out and grabs some different math functions we can use
# #floor method
# #ceil method
# #sqrt method














##########################################################################################
# So what have we learned? We learned some of the basics of numbers in Python. We also learned how to do arithmetic and use Python as a basic calculator. We then wrapped it up with learning about Variable Assignment in Python.
# # **Getting Input from users**
# #how do we get input from users?
# input("what is your name?")
name=input("what is your name")
print("hello",name)
# # basic math calculator
# #ask the user for 2 numbers
num1= int(input("enter a number:"))
num2= int(input("enter another number:"))
# # print out a statement where you:
# # add them together
print(num1 + num2)
# #multiply
print(num1 * num2)
# # find the max number
print(max(num1,num2))
# # find the remainder of the numbers
print(num1 % num2)
# #round one number
print(round(num1))


num3= int(input("enter a number:"))
num4= int(input("enter another number:"))
print(num3 - num4)
print(num3/num4)
print("the min of the third number and fourth numberis",min(num3 + num4))
print("the absolute value of the fourth number is",abs(num4))
print("the floor of your third number is",floor(num3))
print("the ceil of your fourth number is",ceil(num4))
print("the square root of your third number and fourth number is",sqrt(num3 + num4))


color-input("enter a color:")
plural_noun=input("enter a plural noun:")
celebrity=input("enter a celebrity:")



















##########################################################################################
# # mad libs game
# print("Roses are {color}")
# print("{plural noun} are blue")
# print("I love {celebrity}")
# # On to codehs.com






