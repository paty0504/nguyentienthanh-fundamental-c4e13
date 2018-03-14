name = input('Your name: ').lower()
character = name.split()
for i in range(len(character)):
    character[i] = character[i].capitalize()
    word = " ".join(character)
print('Updated name: ', word)
