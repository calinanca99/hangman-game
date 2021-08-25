def return_index(word, letter):
    indexes = []
    for i in range(len(word)):
        if letter == word[i]:
            indexes.append(i)

    return indexes
