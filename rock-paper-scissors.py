# The goal is to create a game of rock paper scissors and in the process learn git & github

import random


print("ROCK PAPER SCISSORS vs PC")
name = input("What's your name? ")
n = int(input("How many rounds would you like to play? ")) 

print("Rule: Type 'rock', 'paper' or 'scissors' to play")


print(f"Okay {name} let's play! \n***************************")

games = 0
score = []

# Each input is assigned a number to make it easier to detect the winner
rules = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

while games < n:

    print(f"Game {games+1}")
    user = input(f"{name} : ")
    user = rules.get(user, -10)    # User assigned -10 if input is invalid
    pc = random.choice(['rock','paper','scissors'])
    print(f'PC : {pc}')
    pc = rules[pc]
    if user == -10:
        print("Please type one of 'rock', 'paper', 'scissors'")
        continue
    elif user == pc:
        print("tie...again!")
    elif (user - pc) == -1:
        print("PC WINS")
    elif (user - pc) == 1:
        print(f"{name} WINS!")
    elif (user - pc) == -2:
        print(f"{name} WINS!")
    elif (user - pc) == 2:
        print("PC WINS")
    
    games += 1
    
        

    
        



