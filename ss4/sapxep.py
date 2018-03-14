list1 = [ 1, 0, -10, 2, 60, 27]
list2 = []
while True:
    list2.append(min(list1))

    list1.remove(min(list1))

    if len(list1) == 0:
        break
print(*list2)
