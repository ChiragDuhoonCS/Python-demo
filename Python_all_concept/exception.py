#!  DAY - 17  EXCEPTION HANDLING
# python "Python_all_concept\exception.py"

try:
    print(10/0)
except:
    print("Eroor")      

try:
    print("A")
    print(10 + "5")
    print("B")

except:
    print("Error")

print("End")


try:
    num = int(input())

except ValueError:
    print("Invalid")

else:
    print("Correct") #@ print when try work


try:
    print(10+"5")

except Exception as e: #@ tell us whats error
    print(e)


#! Spreading

a = [3,5,6]     
b = [3,8,0]

c = [*a,*b]
print(c)

#! enumerate()  for adding indexing
fruits = ['banana','orange','apple']
for index,fruit in enumerate(fruits,start=1):
    print(index,fruit)

#! Zip()  merging two stuff
names=["A","B","C"]

marks=[90,80,70]

for name,mark in zip(names,marks):
    print(name,mark)


