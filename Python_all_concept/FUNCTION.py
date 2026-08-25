#! DAY - 11 FUNCTIONS

#@ return like break after that nothing print

#& *args      
def add(*nums):
	return sum(nums)

y = add (3,5,6,7,4)
print(y)

#&  **Kwargs    for dictionary
def person(**info):
    print(info)

person(name="Chirag",age=17)

#& unpacking dictionary

def greet(name,location):
    return f"Hello {name} from {location}!"

data = {
    "name":"Chirag",
    "location":"Meerut"
}

print(greet(**data))

#& can rename
x = greet
print(x(**data))