'''
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(getAvailableLetters(lettersGuessed))
abcdfghjlmnoqtuvwxyz

Hint: You might consider using string.ascii_lowercase, which is a string comprised of all lowercase letters:
>>> import string
>>> print(string.ascii_lowercase)
abcdefghijklmnopqrstuvwxyz
'''
import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet=string.ascii_lowercase
    for letter in lettersGuessed:
        alphabet=alphabet.replace(letter,'')           
    return alphabet

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
