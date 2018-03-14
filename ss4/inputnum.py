s = input('Enter a sequence of numbers, separated by space:')
# print(*numbers.split())
#strip: cut spaces at start/end of str
words = s.strip().split(' ')
numbers = []
for word in words:
    numbers.append(int(word))
print(numbers)
is_sorted = True
for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        is_sorted = False
        break
    if is_sorted:
        print('Your sequence is already sorted')
    else:
        list2 = []
        while True:
            list2.append(min(numbers))
            numbers.remove(min(numbers))
            if len(numbers) == 0:
                break
        print('Your sequence is not sorted')
        print(list2)
