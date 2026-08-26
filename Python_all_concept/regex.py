#! DAY - 18 REGEX

#  python "Python_all_concept\regex.py"


import re

#@ it just match  only first word
text="Python is awesome"

print(re.match("Python",text))
print(re.match("awesome",text))

#@  search every word   
#@ findll  if same word is more than one it will give us
text="I love Python"

print(re.search("Python",text))

#@ re.sub    replace
text="Python is good"

print(re.sub("Python","Java",text))

#& REGEX SYMBOLS

#[A-Z]  means any capital letter
# [A-Za-z0-9]
#&  \d means digit  if \d+ one or more digits
#&  *  a*   means zero or more
#&  ?  zero or one
#&  $  end of string
#&  ^  means beginning of string 
#&  and if [^abc]  means not a b c
#&  \d{4} means 4 digits






