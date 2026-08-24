#! DAY - 5 LISTS []
#+ can change, ordered,duplication,diff type

letters=["A","A","B","C","D"]
print(letters[0])

#  * *rest used during unpacking

#@ finding stuff
fruits=["apple","banana"]
print("banana" in fruits)

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
#@ SORTED  - change in duplicate not original file



