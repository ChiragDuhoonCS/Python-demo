# python "Python_all_concept\string.py"
#! DAY - 4 STRING

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





