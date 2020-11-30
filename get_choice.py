def getChoice():
    while True:
        choice = input("Do you want to play again? (Y)es or (N)o: ")
        if choice.lower()[0] not in "ny":
            print("ENTER Y for YES and N for NO.")
        else:
            return choice
