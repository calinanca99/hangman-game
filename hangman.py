import random
from play_WORKING import *
from get_choice import *

def main():
    print("-----------Welcome to the Hangman!-----------")
    print("The rules are simple: I think about a word and you have to guess it! You have 5 limbs.\nLet's start!\n")
    words = ['computer', 'house', 'duck', 'muscle', 'mouse', 'wood', 'table', 'window', 'cigarette']
    while True:
        word = words[random.randint(0, len(words)-1)]
        play(word)

        if get_choice().lower()[0] == 'y':
            continue
        else:
            print("Thanks for playing.\nBye!")
            break

if __name__ == "__main__":
    main()
