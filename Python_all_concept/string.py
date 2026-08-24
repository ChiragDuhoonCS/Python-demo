# python "Python_all_concept\string.py"
#! DAY - 4 STRING

#* STRING CANNOT BE CHANGED AFTER CREATED  not exactly see string method

#@ Merger
first_name = 'Chirag'
last_name = 'Duhoon'

full_name = first_name + " " + last_name
print(full_name)
print(len(full_name))

#@ ESCAPE SEQUENCES
#@ \t for tab (space)  
print('Hello\tmy\tname\tis\t\"Chirag\"\nHow')

#@ in len spaces and number (everything) also count 


#* will print exact like that use """ to do that
print("""YO   
      MY NAME IS CHIRAG""")

#@ STRING FORMATING
name = "Alice"
age = 20

print("My name is %s and I am %d years old." % (name, age))

#% USE THIS F-STRING
#* f    { name extracting}
print(f"My name is {name}.")
a = 5
b = 3

print(f"Sum = {a + b}")

pi = 3.141592

print(f"{pi:.2f}") #* SEE : AND {}

#@ INDEXING
language = "Python"

print(language[0]) #* [start:end] end going to miss out
#* [start:end:step]

#@ unpacking
language = "CAT"

a, b, c = language

print(a)
print(b)
print(c)

#@ reverse slicing
language = "Python"

print(language[::-1])

#@ STRING METHOD

#@ CAPITALIZE AND OTHER
name = "python"
print(name.upper()) #* see how we write

#% .lower()  all lower   islower()  to check
#% .swapcase()   Uppercase becomes lowercase and vice versa.
#% .capitalize() only initial word capital
#% .title    capitalizes the first letter of every word.
#% text.lstrip()  remove space from left

#@ REPLACE
text = "I love Java"
print(text.replace("Java", "Python"))

#@ STRING TO LIST   USE SPLIT()   its opposite is join()

#% word - index   find()
#% index - work   index()
#% count word    count()

#@ ASKING   TRUE OR FALSE

print(text.startswith("Py"))

#% isalpha    only alphabet   is digit for digit
#% both letter and digit   isalnum

#% checks whether a string is a valid Python variable name.
"first_name".isidentifier()

#@ Center string   center with -
print(text.center(20, "-"))  

#% Replaces tabs with spaces.
text = "Name\tAge"

print(text.expandtabs(10))










