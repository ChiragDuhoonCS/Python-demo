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
print(A.issubset(B))  # true

#@ SYMMETRIC DIFF     IT REMOVE COMMON ONE
print(A.symmetric_difference(B))

#@ DISJOINT   no common
print(A.isdisjoint(B))  #true






