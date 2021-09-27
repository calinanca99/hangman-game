def try_letter(used_letters):
    while True:
        guess = (input("Guess a letter ---> ")).lower()
        if guess not in "abcdefghijklmnopqrstuvwxyz" or len(guess) != 1:
            print("Please enter ONE LETTER!")
            continue
        else:
            if guess in used_letters:
                print(f"{guess} has been already used.")
                print(f"The used letters are {sorted(used_letters)}")
                continue
            else:
                used_letters.append(guess)
                print(f"The used letters are {sorted(used_letters)}")
                return guess
