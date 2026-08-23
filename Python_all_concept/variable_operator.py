#  python "Python_all_concept\variable_operator.py"

#! DAY-1 BASIC AND TYPE

print("This include all python concept with imp ques")

#@ this is modulus give us remainder
print(3%2)

#@ this is floor division operator 1.5 into 1
print(3 // 2)
#% means go to smaller   alert when negative number

#@ list - dynamic can change can store easily(store ref/pointer)
print(type([23,34,6]))
#% name.append("name we want to add")  to add stuff

#@tuple - fix cant cahnge take low memory
print(type((4,5,6,))) #type like that to get type

#@set - fix cant cahnge take low memory
print(type({4,5,6,})) #type like that to get type

#@dictionary  key:value
print({'Name': 'Chirag'})

#! DAY - 2 VARIABLE

#@ Input from user
#* Write like that (name =) then put in print 
name = input("Enter your name: ")
age = int(input("Enter your age: ")) #* use int and float
city = input("Enter your city: ")

print("Name: ", name)
print(age)
print(city)

#@ CONVERTING ONE TYPE TO ANOTHER
#% new name = type which it going to change(old name)
age_float = float(age)

#@ length of string
print(len(name))

#@ max number (we will create and it will findout max number)
number = 3,27,7365
print(max(number))

#! DAY 3 OPERATOR
#? BASIC CAL
number = int(input("Whats the Number: "))
square = number**2
cube = number**3
division = number/2
floor = number//2
reminder = number % 2
print("Division: ", division)
print("Floor: ", floor)
print("Remainder: ", reminder)

#@ AND - * both follow
#@ OR - +  only one follow
#@ NOT     reverse result

#@ in   Bollen true or false
print("Does your name contain 'a'? ", "a" in name)
print("Does your name contain 'on'? ", "on" in name)

#@compare
print(5 > 2)