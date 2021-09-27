from return_index import *
from letter import *

def play(word):
    used_letters = []
    word = word.lower()
    mask = [i for i in '*' * len(word)]
    limbs = 0

    print(f"Your word has {len(word)} letters!")
    print("".join(mask))

    while '*' in mask:
        letter = try_letter(used_letters)

        if letter in word:
            indexes = return_index(word, letter)

            for i in indexes:
                mask[i] = letter

        if letter not in word:
            limbs += 1
            print(f"WRONG! You have {limbs} limbs.")

        print("".join(mask))

        if limbs >= 5:
            print("You lost!")
            print(f"The word was: {word}")
            break

        if '*' not in mask: ###To end game
            mask = "".join(mask)
            print("You won!")
            print(f"The word was: {word}")
            break
