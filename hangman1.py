
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    word = ''
    for letter in lettersGuessed:
        if letter in secretWord:
            word += letter
    if ''.join(sorted(word))==''.join(sorted(lettersGuessed)):
        return True
    else:
        return False

print(isWordGuessed(secretWord, lettersGuessed))
