letter = 'ThiS is String with Upper and lower case Letters'
split = list(letter.lower())
times = {}
sort = ''.join(sorted(split))
for i in sort:
    if i not in times:
        times[i] = sort.count(i)
for key in times:
    print(key, times[key])
