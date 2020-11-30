def getLetter(usedLetters):
    while True:
        guess = (input("Guess a letter ---> ")).lower()
        if guess not in "abcdefghijklmnopqrstuvwxyz" or len(guess) != 1:
            print("Please enter ONE LETTER")
            continue
        else:
            if guess in usedLetters:
                print(f"{guess} has been already used.")
                print(f"The used letter are {sorted(usedLetters)}")
                print(sorted(usedLetters))
                continue
            else:
                usedLetters.append(guess)
                print(f"The used letter are {sorted(usedLetters)}")
                return guess
