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

