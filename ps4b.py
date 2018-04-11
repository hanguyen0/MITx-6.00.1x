#import ps4a
from ps4a import *
import time


#
#
# Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    bestScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        if isValidWord(word, hand, wordList):
            # find out how much making that word is worth
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if (score > bestScore):
                # update your best score, and best word accordingly
                bestScore = score
                bestWord = word
    # return the best word you found.
    return bestWord

#
# Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    totalScore = 0
    # As long as there are still letters left in the hand:
    while (calculateHandlen(hand) > 0) :
        # Display the hand
        print("Current Hand: ", end=' ')
        displayHand(hand)
        # computer's word
        word = compChooseWord(hand, wordList, n)
        # If the input is a single period:
        if word == None:
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not a single period):
        else :
            # If the word is not valid:
            if (not isValidWord(word, hand, wordList)) :
                print('This is a terrible error! I need to check my own code!')
                break
            # Otherwise (the word is valid):
            else :
                # Tell the user how many points the word earned, and the updated total score 
                score = getWordScore(word, n)
                totalScore += score
                print('"' + word + '" earned ' + str(score) + ' points. Total: ' + str(totalScore) + ' points')              
                # Update hand and show the updated hand to the user
                hand = updateHand(hand, word)
                print()
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print('Total score: ' + str(totalScore) + ' points.')

    
#
# Problem #6: Playing a game
#
#

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)

    Enter n to deal a new hand, r to replay the last hand, or e to end game: n

Enter u to have yourself play, c to have the computer play: u

Current Hand: a s r e t t t
Enter word, or a "." to indicate that you are finished: tatters
"tatters" earned 99 points. Total: 99 points

Run out of letters. Total score: 99 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: r

    """
    count=0
    previous={}
    #a loop to keep program in a cycle
    while True:
        #enter user input either n or r or e
        userInput=input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        
        #when user input is r but there is no hand yet, return a statement and ask for input again
        if userInput=='r' and count==0:
            print('You have not played a hand yet. Please play a new hand first!')

        #when user input is n or r
        elif userInput=='n' or userInput=='r' and count>0:
            #create a hand
            hand=dealHand(HAND_SIZE)
            count+=1
            
            
            #enter second input whether you play or the computer play               
            compInput=input('Enter u to have yourself play, c to have the computer play: ')

            #another cycle loop for this second input
            while True:
                #second input is u: you play
                if compInput=='u':
                    #second input is u and r, replay previous hand
                    if userInput=='r':
                        playHand(previous, wordList, HAND_SIZE)
                        break
                    #second input is just u, start game and break out of loop
                    else:
                        playHand(hand, wordList, HAND_SIZE)
                        previous=hand.copy()
                        break
                #second input is c: computer play
                elif compInput=='c':
                    #second input is r then c, replay previous hand
                    if userInput=='r':
                        playHand(previous, wordList, HAND_SIZE)
                        break
                    #second input is just c, start game and break out of loop
                    else:
                        compPlayHand(hand, wordList, HAND_SIZE)
                        previous=hand.copy()
                        break
                #second input is neither c nor u, tell user invalid input
                else:
                    print('Invalid command.')

        #user input is e: end game, exit function, no return
        elif userInput=='e':
            break
        #if user input is neither n/r/e: invalid input
        else:
            print('Invalid command.')


        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)



'''
a loop to keep program in a cycle

    #enter user input either n or r or e


    #when user input is r but there is no hand yet, return a statement and ask for input again


    # user input is n / r

        #create a hand

        #enter second input whether you play or the computer play               

        #another cycle loop for computer input

            #second input is u: you play

                #when second input is r then u, replay hand from the previous game

                #second input is just u, start game 

            #second input is c: computer play

                #second input is r then c,  replay hand from the previous game

                #second input is just c, start game 

            #second input is neither c nor u, tell user invalid input

    #user input is e: end game, exit function, no return

    #if userInput is not n/r/e and compInput is not c/u: invalid input
'''
