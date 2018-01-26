# -*- coding: utf-8 -*-
"""
Introduction to Python, 6

Created on Sat Jan 23 22:57:01 2018

@author: Claire Kelling

The purpose of this file is to learn dictionaries.

"""

#set working directory
import os
os.chdir('C:/Users/ckell/OneDrive/Penn State/Research/Python/introduction_to_python')

#######################################
## Lists (review)
#######################################
# Lists are like 1-dimensional arrays of numbers, strings, bools, lists, or
# even a mix of all kinds of data types

numList = [2, 3, 5, 8]
numList[0]  # Zero index is the first element in array
numList[-1]  # -1 index is the last element in array

strList = ['a', 'b', 'c']  # List of strings
strList[2]  # Index the 3rd element in the list
boolList = [True, False, False, True]  # List of booleans
listList = [[1, 2], [8, 3], [7, 4]]  # List of lists

#can create a mix of data types in a list
mixList = [0, 1, 2, 'cat', 'dog', 'bun', True, False, None, [0, 1, 2]]

#########################################
## Dictionaries
#########################################

# Dictionaries are essentially associative arrays, where an index is paired
# with a corresponding value. Dictionaries have no particular order.
# Dictionaries are indexed by their "keys" which must be strings

#notice the data type is "dict"
houseNum = {'Bob': 123, 'Sue': 203}

# Index a dictionary by its key (a string)
#    tell you corresponding value with that string
houseNum['Bob']
houseNum['Sue']

# Indexing with a number does not work on dictionaries
houseNum[1]  # this will result in a KeyError

# Assignment/addition to a dictionary
houseNum['Cam'] = 102

# Remove dictionary elements with "del" function, note different function notation
del houseNum['Bob']

houseNum.keys()  # view keys in dictionary, creates a dict_keys object
houseNum.items()  # view all items (keys and values) in dictionary

# Indexing does not work on a dict_keys object
houseNum.keys()[0] #results in error

# However you can convert a dict_keys object into a list instead and index that
list(houseNum.keys())
list(houseNum.keys())[0]  # index first element
list(houseNum.keys())[-1]  # index last element

# Note that this list is in the order the dictionary was created.
# You can instead sort the dictionary with the sorted function
sorted(houseNum.keys())  # sorts alphabetically
sorted(houseNum.keys())[0]  # index first element alphabetically
sorted(houseNum.keys())[-1]  # index last element alphabetically

#can also make a list of things that go with Bob
houseNum = {'Bob': [123, 'cat', 'pizza'], 'Sue': [203, 'dog', 'pizza']}
