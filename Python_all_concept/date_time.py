#!  DAY - 16  DATE AND TIME

# python "Python_all_concept\date_time.py"

from datetime import datetime



now = datetime.now()
print(now)

new_year= datetime(2033,7,6)

happy_birthday = datetime(2008,11,4)
print("Happy Birthday Chirag ", happy_birthday.strftime("%d/%B/%y,%A"))

from datetime import date
print(date.today())

#@ arthematic in datetime

now = now.date() #& acess today date like that
my_birthday = date(2008,11,4)
print("im that day alive: ",now-my_birthday)


