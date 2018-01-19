# -*- coding: utf-8 -*-
"""
Introduction to Python, 2
Created on Thu Jan 18 20:53:02 2018

@author: Claire Kelling

The purpose of this file is to learn how to create lists and for loops.
"""

# Input/Eval (evaluate) Input
# input asks the user to enter something into the console, 
#     and stores it as a variable
# type says int, string, list, or float
# a float is a double precision number (not an integer)
c = input("Enter a number: ")
type(c)

# eval tries to convert a string into a number
# now this variable is an int, instead of a string
d = eval(input("Enter a number: "))

##################
### Data Types
##################
type(d)
type('3')
type(3)
type(3.1)
# int converts a float to an integer (essentially rounds it)
# if you do a round on a regular float, it stays a float
int(3.1)
#converts an integer to a float
float(3)

##################
### Lists/indexing lists
##################
# creating a list, similar to a vector in R
q = [1, 2, 3, 4]
len(q) #length of q
# *** Python indices start at 0
# the last element is indice (length of list) - 1
q[1] 
q[0]
q[3]
q[4]

# you can access the last of an array using -1
q[-1]
q[-2]
q[-4]
q[-5] # out of range

#to look at a range of values
q[0:2]
q[0:4] # the second index "up until" so including elements 0,1,2,3
q[0:4:2] # 0th element to 4th (but not including) in increments of 2
q[0::2] # this doesn't have an end, so gets every second element until end of list
q[::2] # doesn't have beginning, so gets every second element

w = [1, 2, 3, 4, 5, 6, 7, 8, 9]
w[0::3]
w[2::3]

# empty list
z = []
len(z) #length 0
# Can add or remove values in a list
z.append(3) # add single element
z
z.append(7)
z
z.remove(7)
z
z.append(1)
z.append(1)
z.append(3)
z
z.remove(1) #removes the first value in the list
z
z.append("words") # can also append different data types
z
z[0] # access values again
z[1]
# sub index of the list element, can index strings like lists
z[3][2] 

# can also have lists within lists
a = [1, 2]
b= [3, 4]
c= [a, b] # list of lists

##################
### For Loops
##################

#creating a list
myList = [2, 3, 5, 8, 13]

# there are no brackets in Python
# tabs keep track of the nesting structure
# the following uses my list from above as the indexing variable
#     You need a colon after the loop or conditional statement ***
#     Also, you cannot run individual lines, must be run together
for n in myList:
    print(n)

for i in range(10): #indexes from 0 to 9
    print(i)
    
for j in range(len(myList)):
    print(myList[j])
    
for n in str1: # can index through strings as well
    print(n)

for n in range(len(str1)):
    print(n, ':', str1[n]) # this uses 0 to 4 indexing, instead of through a string
