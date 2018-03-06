h = (int(input('Your heigth in centimeter? '))*0.01)
w = int(input('Your weight in kilogram? '))
bmi = w/(h*h)
print('Your BMI is: ', bmi)
if bmi < 16:
    print('Severely underweight')
elif bmi < 18.5:
    print('Underweight ')
elif bmi < 25:
    print('Normal')
elif bmi < 30:
    print('Overweight')
else:
    print('Obese')
