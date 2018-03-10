from random import choice
from random import shuffle
words = [':v', 'blablabla', 'ahihi']
playing = True
while True:
    word = choice(words)
    correct = word
    character = list(word)
    shuffle(character)
    word = "".join(character)

    print("The jumble is:", word)
    guess = input("Your guess: ")
    if guess != correct:
        print(":(")
    else:
        print("Hura")
        break
