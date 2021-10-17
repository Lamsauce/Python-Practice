"""
===== EXERCISE #3 =====
Write a Python program to display the current date and time.
Sample Output :

Current date and time :
2014-07-05 14:34:14

"""




import datetime

d = datetime.datetime.now()

print("Current date and time : ")
print(d.strftime("%Y-%m-%d %H:%M:%S"))








"""
===== RESOURCE(S) =====
https://docs.python.org/3/library/datetime.html

"""