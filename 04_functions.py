# -*- coding: utf-8 -*-
"""
Introduction to Python, 4

Created on Sat Jan 20 20:57:01 2018

@author: Claire Kelling

The purpose of this file is to learn how to create functions in Python.

"""

#set working directory
import os
os.chdir('C:/Users/ckell/OneDrive/Penn State/Research/Python/introduction_to_python')

#####
## Basics of functions in Python
#####


def main():
    # do something within function
    # According to Pep8 guidelines, functions should have two returns before
    # and after the definition, as illustrated here
    # in Python, it is convention to have one main function, and sub-functions within that 
    #     in a certain order
    print('Hello world')


main()  # run main function
main(12)  #need to match input to what function is expecting

def timesTwo(x):  # value in parentheses is an input
    return 2*x  # variables are outputted using "return" function, does not need parentheses like R


timesTwo(10)  # Run "timesTwo" function with 10 as input

a = 5  # Define some variable
b = timesTwo(a)  # Run function and store as new variable


def sumThreeNums(m, n, p):  # use multiple inputs by separating with commas
    return m+n+p  # can perform math operations within "return" statement


sumThreeNums(1, 2, 3)  # test "sumThreeNums" function


def squareRoot(x):  # function to return positive and negative sqrts
    import math  # can import libraries within a function
    root1 = math.sqrt(x)  # take square root
    root2 = -math.sqrt(x)  # take -1*square root
    return root1, root2  # return both values, separated by commas
    #return root2        # You need to return all variables in the same line, only returns first one


a, b = squareRoot(9)  # run function and store values as variables
a
b
squareRoot(sumThreeNums(2, 3, 4))  # can do functions within functions


def makeZeroList(x):  # little function to demonstrate making a list of 0s
    return [0]*x #list with a certain number of 0 elements


makeZeroList(5)  # test out the function with 5 as an input
a = makeZeroList(5)  # assign value to variable a
a

# In Python, None is used to indicate empty
a = [2,3,None,4]
a[2] == None

################################################
# Important, "pythonic" way of using functions #

# Note, the functions below don't really do anything, so running them isn't
# super useful. Pay more attention to the structure of this code

# The purpose of this code is to use functions in an appropriate, Pythonic way
# and to illustrate the "__name__" construct

# However, the section at the bottom will execute only when this code is run
# directly. This allows the script to be used for this particular purpose, while
# the functions themselves can be called for other purposes.


# The functions below can each be imported into another Python code and called.
#    A module in Python is like a package in R
import func_4b_test_function
func_4b_test_function.main()

# Ways of importing specific functions
from func_4b_test_function import main
main()

## This is an example of how this would be useful
# These functions could be ordered
def startFunction(x):  # Define a function that you want to use
    myList = [0]*x  # initialize list of zeros with length x
    return myList  # return list of zeros


def middleFunction(myList):  # Define some other function
    for n in range(len(myList)):
        myList[n] = n  # write index of array into array
    return myList


def lastFunction(myList):  # Define another function
    tot = sum(myList)
    maxVal = max(myList)
    return tot, maxVal


def main():
    myNum = startFunction(5)
    myList = middleFunction(myNum)
    tot, maxVal = lastFunction(myList)
    print('The input value was {}'.format(maxVal))
    print('The sum of values up to {} is {}'.format(maxVal, tot))


if __name__ == "__main__":
    # This code only runs when this file is run directly
    main()