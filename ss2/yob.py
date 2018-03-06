yob = int(input("Your year of birth? "))
age = 2018 - yob
print("Your age:", age)
if age < 10: #conditional statement
    print('Baby')
elif age < 18:
    print('teenager')
elif age == 24:
    print('Lay chong thoi')

else:
    print("Not baby")
print('Bye')
