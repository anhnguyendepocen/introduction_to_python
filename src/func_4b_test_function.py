"""
Introduction to Python, 4b

Created on Sat Jan 20 20:57:01 2018

@author: Claire Kelling

The purpose of this file is to create a test function, to be called in another file

"""

def myFunction():
    print ("This is my function")
    
    
def main():
    myFunction()
    print("This is my main function")
    
if __name__ == "__main__":    
    print("This is me running the file directly")
else:
    print("This is me running the file indirectly")
