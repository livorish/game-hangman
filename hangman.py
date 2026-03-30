import random
from ctypes import pythonapi
import re

ls_words = ['mother', 'father', 'daughter', 'pineapple', 'orange', 'tiger']
# ls_words = ['pineapple']

man = [
    '''
     +---+
     |   |
         |   
         |
     =====
    '''
    ,
    '''
     +---+
     |   |
     o   |   
         |
         |
         |
     =====
    '''
    ,
    '''
     +---+
     |   |
     o   |   
     |   |
         |
         |
     =====
    '''
    ,
    r'''
     +---+
     |   |
     o   |   
   / |   |
         |
         |
     =====
    '''
    ,
    r'''
     +---+
     |   |
     o   |   
   / | \ |
         |
         |
     =====
    '''
    ,
    r'''
     +---+
     |   |
     o   |   
   / | \ |
    /    |
         |
     =====
    '''
    ,
    r'''
     +---+
     |   |
     o   |   
   / | \ |
    / \  |
         |
     =====
    '''
]

random_word = random.choice(ls_words)

word_with_blank = []
for letter in random_word:
    word_with_blank.append(letter.replace(letter, "_"))

print(random_word)
print(*word_with_blank)
attemption = len(random_word)
length = len(random_word)
i = 0

while attemption > 0:
    attemption -= 1
    guess = input("Guess a letter: ")

    if guess in random_word:
        positions = []
        for match in re.finditer(guess, random_word):
            positions.append(match.start())
        for i in range(len(positions)):
            word_with_blank.insert(positions[i], guess)
            word_with_blank.pop(positions[i] + 1)
        print(*word_with_blank[0:len(random_word)])
        if "_" not in word_with_blank:
            print("You win!")
            break
        if attemption < 1:
            print("You lose, what ashamed!")

        print(f"{attemption}/{length} LIVES LEFT")
    else:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(f"{attemption}/{length} LIVES LEFT")
        if attemption < 1:
            print("You lose, what ashamed!")
            break
        else:
            print(man[i])

    i += 1
