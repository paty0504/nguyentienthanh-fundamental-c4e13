n = int(input("Enter a number: "))

count = 0
if n == 0:
    count =1
else:
    while True:
        n = n // 10
        count += 1
        if n == 0:
            break

print(count)

# count = 0
# while count > 3:
#     count += 1
