# -*- coding: utf-8 -*-
"""
Introduction to Python, 3

Created on Thu Jan 18 20:57:01 2018

@author: Claire Kelling

The purpose of this file is to learn how to do logical operations 
   and if statements/while loops.

"""

#####
## Basics of logic in Python
#####

2 == 3
2 == 2
2 > 3
2 >= 2 #greater than or equal to
2 != 3 #not equal to
2 != 3 and 2 < 3
2 != 3 or 2 > 3
True
False
True and False
True or False
False and False

# Checking if a string is in another string
str1 = 'hello'
'h' in str1 
'hell' in str1
'q' in str1
'q' not in str1 

# Checking if a value is in a list
primes = [2, 3, 5, 7, 11, 13, 17]
3 in primes
4 in primes
4 not in primes

#####
## If Statements
#####
a = eval(input("Enter 2 or any other number: "))  # Ask user for some number
if a == 2:
    print('a is equal to 2') #doesn't do anything if a not equal 2

a = eval(input("Enter 2 or any other number: "))  # Ask user for some number
if a == 2:
    print('a is equal to 2')
else: # ifelse statement
    print('a is not equal to 2')

#Also, we can use else if (syntax is elif)
a = eval(input("Enter 2 or any other number: "))  # Ask user for some number
if a == 2:
    print('a is equal to 2')
elif a == 3:
    print('a is equal to 3')
else: # ifelse statement
    print('a is not equal to 2 or 3')

####
## While loops
####

a = 1
while a != 8:
    print(a)
    a = a + 1
    print('...')
print('Congratulations.') # when it is finished

a = 2
while a < 7:
    a += 1 #shorthand for the a = a+1
    print(a)

a = 1
while a <= 32:
    a *= 2 # shorthand for a = 2a
    print(a)