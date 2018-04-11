#Printing Out the User's Guess
'''
>>> secretWord = 'apple' 
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(getGuessedWord(secretWord, lettersGuessed))
'_ pp_ e'
'''

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    empty='_ '
    newWord=''
    word=secretWord
    for letter in word:
        if letter not in lettersGuessed:
            letter=empty
        newWord+=letter
    return newWord
    
secretWord = 'apple'    
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord,lettersGuessed))
