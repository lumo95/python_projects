# Name: Coin Toss
# Created By: Luke Molloy
# Date: 17/08/16
# Desc: A simple coin toss game, random results every time e.g heads or tails

import random
import time

loop = 1
firstLoop = True


def flip():
    guess = input("\nEnter your guess! (Heads/Tails)\n").upper()
    
    while guess != "HEADS" and guess != "TAILS":
        guess = input("\nInvalid guess! Enter your guess! (Heads/Tails)\n").upper()
    
    print("\nA coin is tossed..\n")
    time.sleep(1)
    print("..it lands on..\n")
    time.sleep(1)
        
    res = random.randint(1, 2)
    if res == 1 and guess == "HEADS":
        print("\nHeads! You win!")
    elif res == 1:
        print("\nHeads! You lose!")
            
    if res == 2 and guess == "TAILS":
        print("\nTails! You win!")
    elif res == 2:
        print("\nTails! You lose!")

# while loop is used to ensure the program runs until the user chooses to exit

while loop == 1:
    if firstLoop is True:
        print("Welcome to Coin Toss. Ready to flip a coin? (yes/no)")
        firstLoop = False
        
    else:
        ans = input().upper()

        while ans != "YES" and ans != "NO":
            ans = input("\nInvalid answer. Please type YES or NO\n").upper()
        if ans == "YES":
            flip()
            time.sleep(1)
            print("\nDo you want to toss it again? (yes/no)")
        else:
            print("\nYou are leaving the game! Have a good day!")
            time.sleep(2)
            exit()
