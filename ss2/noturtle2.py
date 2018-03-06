for i in range(6):
#     for j in range(i):
#         print('* ', end='')
#     print()
    for j in range(6):
        if j >= 7 - i:
            print("* ", end='')
        else:
            print( '', end='')
    print()
