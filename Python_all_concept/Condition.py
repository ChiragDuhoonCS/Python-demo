#!  DAY - 9  CONDITIONALS
#  python "Python_all_concept\Condition.py"

name = input("Name: ")
age = int(input("Age: "))
marks = int(input("Marks: "))

print(f"Name is {name}")
print(f"Age is {age}")
print(f"Marks is {marks}")

if age >= 18: print('You are adult')

if marks > 50 and age >= 18: print("You are elligible to take admission")
elif marks > 50 and age < 18: print("You are minor")
else: print("You cant take admission")