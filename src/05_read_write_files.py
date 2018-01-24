# -*- coding: utf-8 -*-
"""
Introduction to Python, 5

Created on Sat Jan 23 20:57:01 2018

@author: Claire Kelling

The purpose of this file is to learn to read/write files in Python.

"""

#set working directory
import os
os.chdir('C:/Users/ckell/OneDrive/Penn State/Research/Python/introduction_to_python')

##########################################
## Reading a file
##########################################

# Reading a 1D list of numbers as a list
fname = 'data/acc2.dat'  # select name of file
infile = open(fname, "r")  # open file with "read" access
longStr = infile.read()  # read contents of file into one long string

# separate long string into discrete values
# split the string at the "newline" character
data = longStr.split('\n')  #this is a list
infile.close()  # VERY IMPORTANT - close the file when you're done with it
#this is so that it can be used in other programs and it uses less memory

data
len(data)  # look at length of data

#the last line is empty (need to remove it twice as there are two empty values)
#data.remove("")
#data.remove("")

#OR you can use the filter function
data = list(filter(None, data))
len(data) #removed two empty values

#need to convert the strings to floats (non-integer numeric)
data = list(map(float, data)) #(data type we are converting to, list being converted)
min(data)  # find minimum value
max(data)  # find maximum value

##########################################
## Writing to a file
##########################################

a = list(range(10))

# opens (and creates in this case) file object with write access (w)
f = open('data/05_write_example.txt', 'w')

# the .write method requires a string as input
# note: .write will overwrite an existing file
# to append to a file instead, use .append
for n in range(len(a)):
    f.write(str(a[n])+'\n')  # one method is to write strings to files
                             #\n is a newline character
    
f.close()  # close the file

# Using ".format" to write more elegantly to a file
x = [1., 10., 100., 1000., 10000.] #1. makes them float format, rather than int format
y = [1., 2., 3., 4., 5.]
z = [0.123, 0.456, 0.789, 0.135, 0.246]

f = open('data/05_write_example2.txt', 'w')

#making a string, this will be the column headers
f.write('{}, {}, {}\n'.format('x', 'y', 'z'))

for n in range(len(x)):
    f.write('{}, {}, {}\n'.format(x[n], y[n], z[n]))
    
f.close()


# Now make it even nicer by specifying field widths
f = open('data/05_write_example2_nicer.txt', 'w')

#gives each character five spaces
f.write('{:5}, {:5}, {:5}\n'.format('x', 'y', 'z'))


for n in range(len(x)):
    # gives characters 5 spaces each
    f.write('{:5}, {:5}, {:5}\n'.format(x[n], y[n], z[n]))
    # can also specify number of decimals
    #f.write('{:5.0}, {:5}, {:5}\n'.format(x[n], y[n], z[n]))
    
f.close()


# Further, you can specify the (maximum) number of decimals
#    This example truncates the z variable at 1 decimal
# this example goes to using the print function (to avoid making another file)
print('{:10}, {:10}, {:10}\n'.format('x', 'y', 'z'))
for n in range(len(x)):
    print('{:10}, {:10}, {:10.1}\n'.format(x[n], y[n], z[n]))


# the number before the column is which input you are selecting to put here
# the number after the column is how many characters you are giving this input
print('{1:5}, {2:5}, {0:5}\n'.format('x', 'y', 'z'))
# this places 'y' first, then 'z', then 'x'
for n in range(len(x)):
    print('{1:10.0}, {2:10}, {0:10}\n'.format(x[n], y[n], z[n]))
    
 