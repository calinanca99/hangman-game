def return_index(word, letter):
    """
    Helper function in the unmasking of the word.
    """
    indexes = []
    for i in range(len(word)):
        if letter == word[i]:
            indexes.append(i)

    return indexes
