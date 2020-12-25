"""
File: hangman.py
Name: Jeffrey.Lin 2020/08
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    This game gives players several chances to win the word guessing games.
    If the player loses, the man will be hanged.
    """
    # import random word to be the answer of the game.
    answer = random_word()
    ans = ''
    for i in answer:
        ans += '_'
    print('The word looks like:'+ans)
    print('You have ' + str(N_TURNS) + ' guesses left.')
    # number of error
    num = 0
    while True:
        input_ch = input('Your guess: ')
        # make the input words to be uppercase letter.
        input_ch = input_ch.upper()
        length = len(input_ch)
        # check the input word
        if length == 1 and input_ch.isalpha():
            i = answer.find(input_ch)
            if i != -1:
                for i in range(len(answer)):
                    if answer[i] == input_ch:
                        ans = ans[: i] + input_ch + ans[i + 1:]
                print('You are correct!')
                if ans != answer:
                    print('The word looks like:' + ans)
                    print('You have ' + str(N_TURNS - num) + ' guesses left.')
                else:
                    print('You win!!')
                    print('The word was: ' + answer)
                    break
            else:
                num += 1

                if N_TURNS - num == 0:                                  # run out of opportunities
                    print("There is no " + input_ch + "'s in the word.")
                    print('You are completely hung :(')
                    print('The word was: ' + answer)
                    break
                else:
                    print("There is no " + input_ch + "'s in the word.")
                    print('The word looks like:' + ans)
                    print('You have ' + str(N_TURNS - num) + ' guesses left.')

        else:
            print('illegal format.')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
