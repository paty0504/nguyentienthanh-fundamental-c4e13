n = int(input('Enter a number? '))
if n < 0:
    print('No factorial')
elif n == 0:
    print('The factorial of O is 1')
else:
    f = 1
    for i in range(1, n + 1):

        f = f*i
    print('The factorial is: ', f)
