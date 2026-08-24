#! DAY - 5 LISTS []
#+ can change, ordered,duplication,diff type

letters=["A","A","B","C","D"]
print(letters[0])

#  * *rest used during unpacking

#@ finding stuff
fruit=["apple","banana"]
print("banana" in fruit)

#& MAXIMUM STUFF SAME AS STRING 

del letters[1] # can delete whole list
#@ use clear to clear all element with list also exist
print(letters)

b = letters.copy
print(b) #any changes in b wouldnt affect a

#@ count  - count recursion
print(letters.count('A'))

#@  SORT  VS SORTED
#@ SORT  - change in original file
letters.sort(reverse=True)
print(letters)

#@ SORTED  - change in duplicate not original file
y = letters.sorted(reverse=True)
print(y)
print(letters)


#! DAY - 6  TUPLES()
#@ cannot cahnge  faster 

fruits = ("apple", "banana", "mango")
#* use x = (4 ,) when we try to find type

# means 1 and onward
print(fruits[1:])
print(fruits[-2:]) # last two print

#* MODIFY TUPLE (convert to list then tuple again)
fruits = ("apple","banana","mango")

fruits = list(fruits)
fruits[0] = "pineapple"

fruits = tuple(fruits)
print(fruits)


#@ Unpacking
person = ("Chirag",20,"India")

name, age, country = person

print(name)
print(age)
print(country)


#* Nested Tuple
student = (
    "Chirag",
    (90,95,88),
    "India"
)
print(student[1][0])





