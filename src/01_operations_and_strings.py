# -*- coding: utf-8 -*-
"""
Introduction to Python 1
Created on Thu Jan 11 20:06:11 2018

@author: Claire Kelling

The purpose of this file is to learn to make variables and how 
to use basic operations and strings.
"""

######################################################################
### Basic Operations and Variable Storage 
######################################################################

# assigning variables
a = 2
b = 3

# displaying variables
print(a)

# doing basic math operations
a+b
print(a+b)
a-b
a*b
a/b
a^b # this is not exponent, this is 
a**b # this is the exponent function
#2a, this produces an error, need a *
2*a

#how to round numbers
round(3.1)
round(3.5)
# sqrt(a), sqrt is not included in the default package

# we need to import a package to use sqrt as well as other functions
import math

math.sqrt(a)
math.cos(a)
math.ceil(3.1)
math.floor(3.5)
math.floor(3.99999)
round(3.999999)

import math as m # I can name a package a shortcut version
m.sqrt(a)

from math import sqrt # this imports a single function and doesn't require using math.function

sqrt(a)

#You can also import several functions from one package
from math import sqrt, cos

#Imaginary numbers
1j # this is the equivalent to "i", j is not recognized by itself
1j**2
sqrt(-1) #this returns an error with the standard square root function
(-1)**(1/2) #this is close to 0 + j, numerical rounding issue

import cmath # I can import and overwrite the previous sqrt function
cmath.sqrt(-1) #now it returns the correct answer, instead of an error

from cmath import sqrt
sqrt(-1) #overwritten function

# NOT RECOMMENDED but you can import everything from a package into the space
#from math import *
#sqrt(a)
#cos(a)

######################################################################
### Strings
######################################################################
str1 = 'hello' # can do single or double quotes
str2 = "there"
str1 + str2
str1 + ' ' + str2
str3 = str1 + ' ' + str2

type(a) #need to figure out what type of variable a is (str, int, float, bools, lists)
a = str(a) #need to convert a to a string, instead of a int
type(a) #it is now a str

str1 + ' ' + a

print(str1)

# how many characters are in the string
len(str1)

#this dot notation is a method that is executed on an object, similar to a function

str1.split('e') #splits it into two parts, stores it in a list
str3 = 'How do you do?'
str3.split(' ') #4 words in this string, all stored in a list

str3.upper() # function, makes it all upper case
