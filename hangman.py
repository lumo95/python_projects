# Name: Hangman
# Created By: Luke Molloy
# Date: 16/08/16
# Desc: A simple guess the word program, similar to the popular 'Hangman'

guessWord = input("Please enter the hangman's word!\n").upper()  # word to be guessed
display = ["*"] * len(guessWord)  # amount of astrix' to show
userGuess = ""  # users guess

guessLimit = 20

guesses = []


def check_input(x):

    while len(x) > 1 or x in guesses:
        if x in guesses:
            x = str(input("You have already guessed " + x + " Try another!\n").upper())

        if len(x) > 1:
            x = str(input("You can only guess one letter at a time E.g 'A'\n").upper())

    return x


def play_game(guess, lim):

    correct = 0
    counter = 0

    while guess != "END" and lim != 0:

        print("The word is: " + ''.join(display) + "\n")
        guess = str(input("Enter a letter: \n").upper())
        guess = check_input(guess)

        if correct != len(guessWord):
            print("\nYou have ", lim, " guesses left.")

        guesses.append(guess)

        while counter < len(guessWord):

            if guessWord[counter] == guess:
                display[counter] = guess
                correct += 1

            counter += 1

        lim -= 1
        counter = 0

        if correct == len(guessWord):
            print("Winner!\nThe word was: " + ''.join(display))
            break

        if guessLimit == 0:
            print("You're out of guesses! Game over!")


play_game(userGuess, guessLimit)
