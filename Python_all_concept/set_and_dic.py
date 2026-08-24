#!  DAY - 7  SETS{}
#@ unordered , remove add no index, can print repeatation

#& UPDATE OR ADD
# @ use update to add multiple stuff
# @ use add to add single stuff

#& REMOVE OR DISCARD
#@ remove raise error if stuff not exist
#@  discard doesnt

#& POP  discard(remove) random element

#& REMOVE DUPLICATION BY CHANGING TYPE
numbers = {3,5,5,3,6,6,6}
print(numbers)

numbers = list(set(numbers)) 
print(numbers)

#&  SET OPERATOR

#@ UNION  it create new set
#@ UPDATE  cahnge A itself
A = {1,2,3}
#> means  OR
B = {3,4,5}

print(A.union(B))  #> doesnot print repeatition

#@ INTERSECTION   Common one

#@ SUBSET     SUPERSET OPPOSITE
print(A.issubset(B))  

#@ SYMMETRIC DIFF     IT REMOVE COMMON ONE
print(A.symmetric_difference(B))

#@ DISJOINT   no common
print(A.isdisjoint(B))  

#! DAY - 8 DICTIONARY

python_student = {
    "name":"Chirag",
    "age":20,
    "course":"Python",
    "address" : {          # seee nested here
        "city":"Meerut",
        "state":"UP"
    }
}
#always use [] to access in distionary 
#no indexing but we can create list inside it which have indexing 
## adding things in distionary
python_student["personality"] = "cool"
print(python_student)

## changing data   modify stuff
python_student["age"] = 22
print(python_student["age"])

## lenth
print(len(python_student)) #answer is 3
print(len(python_student["name"]))  #answer is 6

## accecing nested stuff
print(len(python_student["address"]["city"]))  # see here 

##new thing   it doesnt add in distionary
print(python_student.get("gender"))   # answer is none
print(python_student.get("gender","male"))

## in
print("name" in python_student)
print("rag" in python_student["name"]) #nested

## remove stuff
python_student.pop("age")  #  age vanish from it


##remove last inserted thing   that is persanolity here
python_student.popitem()
print(python_student)

## to delete entire distonary   prefered
#del python_student["age"]
#del python_student()

## items  to convert distionary into tuples
print(python_student.items())  #helpful for loops

## clear
# it exist but dont hold anything

## copy one distionary to another
#python_student2 = python_student.copy()

## extract only key value
print(python_student.keys())


## extract only values
print(python_student.keys())








