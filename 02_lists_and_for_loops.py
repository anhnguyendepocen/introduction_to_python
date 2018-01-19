# -*- coding: utf-8 -*-
"""
Introduction to Python 2
Created on Thu Jan 18 20:53:02 2018

@author: Claire Kelling

The purpose of this file is to learn how to create lists and for loops.
"""

Input/Eval Input

c = input(‘Enter a number: ‘)

type(c)

d = eval(input(‘Enter a number: ‘))

type(d)
type('3')
type(3)
type(3.1)
int(3.1)
float(3)

Lists/indexing lists

q = [1, 2, 3, 4]
len(q)
q[1]
q[0]
q[3]
q[4]
q[-1]
q[-2]
q[-4]
q[-5]
q[0:2]
q[0:4]
q[0:4:2]
q[0::2]
q[::2]

w = [1, 2, 3, 4, 5, 6, 7, 8, 9]
w[0::3]
w[2::3]

z = []
len(z)
z.append(3)
z
z.append(7)
z
z.remove(7)
z.append(1)
z.append(1)
z.append(3)
z
z.remove(1)
z
z.append(‘words’)
z
z[0]
z[1]
z[1][2]
str1[0:3]

For loops

myList = [2, 3, 5, 8, 13]
for n in myList:
    print(n)

for i in range(10):
    print(i)
	
for n in str1:
    print(n)

for n in range(len(str1)):
    print(n, ':', str1[n])

for j in range(len(

Logical operations

a == b
a > b
a >= b
a != b
a != b and a < b
a != b or a < b
True
False
True and False
True and True
False or True
False and False

str1
‘h’ in str1
‘q’ in str1
‘q’ not in str1

If statements

if a == 2:
    print(‘a is equal to 2’)

if a == 2:
    print(‘a is equal to 2’)
else:
    print(‘a is not equal to 2’)

While statements

while a < 10:
    a = a + 1
	print(a)

a = 2

while a < 10:
    a += 1
    print(a)

a = 2

while a < 25:
    a *= 2
    print(a)

Order/characters

ord('a')

ord('b') 

ord(‘A’) 

chr(97)

for n in range(50, 100):
    print(chr(n))

chr(ord(‘a’))
chr(ord('a')+1)
chr(ord('a')+10)

alphabet = []
m = 0
while ‘z’ not in alphabet:
alphabet.append(chr(ord('a') + m))
	m += 1
	print(alphabet)

'z' in alphabet
'Z' in alphabet
'Z'.lower() in alphabet

Function definitions, inputs, and outputs

def main():
    # do something
	print(‘Hello world’) # btw this is a comment

main()

def timesTwo(x):
    return 2*x

timesTwo(10)

def sumThreeNums(m, n, p):
	return m+n+p

sumNumbers(1, 2, 3)

def squareRoot(x):
	import math
	root1 = math.sqrt(x)
	root2 = -math.sqrt(x)
	return root1, root2

a, b = squareRoot(9)
a
b

squareRoot(sumNumbers(2, 3, 4))

PEP8 online check

http://pep8online.com/

Read simple files (1D list)

fname = ‘acc2.dat’
infile = open(fname, "r")
longStr = infile.read()
data = longStr.split(‘\n’)
infile.close() # VERY IMPORTANT 

len(data)
max(data)
min(data)

import statistics as stat
stat.mean(data)

Why the error? Need to convert to list of floats instead of strings

data2 = list(map(float, data))
data2

or use LIST COMPREHENSION (useful concept)
data3 = [float(i) for i in data]
data3

data2 – data3  # should be zero, right?

result = [data2[i] - data3[i] for i in range(len(data2))]



Plotting with MatPlotLib

import matplotlib.pyplot as plt
plt.plot(data)

import numpy as np
plt.plot(range(100, 200), data)

plt.plot(range(0, 500, 10), data)
