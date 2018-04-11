'''
mistakesMade: The number of incorrect guesses made so far.

Loading word list from file...
	55900 words loaded.
	Welcome to the game Hangman!
	I am thinking of a word that is 4 letters long.
	-----------
	You have 8 guesses left.
	Available Letters: abcdefghijklmnopqrstuvwxyz
	Please guess a letter: a
	Oops! That letter is not in my word: _ _ _ _

	Sorry, you ran out of guesses. The word was else. 
'''

def mistakesMade(word):
    for i in range(8, 0, -1):
        print('You have ' + str(i) + ' gueses left.')

    print('Sorry, you ran out of guesses. The word was ' + word)
mistakesMade('else')
