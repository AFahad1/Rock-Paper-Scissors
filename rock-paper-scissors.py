# The goal is to create a game of rock paper scissors.
# the aim is to get to learn github
# Step 1: create an MVP

import random


print("ROCK PAPER SCISSORS vs PC")
print("Rules: \n TYPE rock, paper or scissors to play, but first")
name = input("What's your name? ")
rules = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}


n = int(input("How many games would you like to play? ")) 

print(f"Okay {name} let's play!")

for i in range(n):
    print(f"Game {i+1}")
    user = input(f"{name} : ")
    pc = random.choice(['rock','paper','scissors'])
    print(f'PC : {pc}')
    user = rules.get(user, -10)
    pc = rules[pc]
    if user == pc:
        print("tie...again!")
    elif (user - pc) == -1:
        print("PC WINS")
    elif (user - pc) == 1:
        print(f"{name} WINS!")
    elif (user - pc) == -2:
        print(f"{name} WINS!")
    elif (user - pc) == 2:
        print("PC WINS")
    else:
        print("Please type one of 'rock', 'paper', 'Scissors'")
    
        



