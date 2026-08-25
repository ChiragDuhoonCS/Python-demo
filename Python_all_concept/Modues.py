#! DAY - 12  MODULES
# python "Python_all_concept\Modues.py"

# this is module   just .py file
def add(a, b,c):
    return a + b + c

def sub(a, b, c ):
    return a - b

PI = 3.14159

print(add(5,4,6))
print(sub(5,4,6))
print(add(5,4,6)*PI)

#&  IMPORT FROM ANOTHER .py
#@  import mudule_name
#@  module_name.its_function 

import FUNCTION 
print(FUNCTION.greet)

import math as m # nickname
# to import specific from math import sqrt as s
# import everything   from math import *
print(m.sqrt(25))

#!  OS MODULE  talk to operating system
import os 
os.getcwd()
os.chdir("Python_all_concept")
print(os.getcwd())  #to varify

#os.rename("tempCodeRunnerFile.py","temp.py")


#! Sys Module
import sys
print(sys.version)
print(sys.path)

print("Hello")

sys.exit()

print("World")

