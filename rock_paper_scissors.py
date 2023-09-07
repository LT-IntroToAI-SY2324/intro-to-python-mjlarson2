# We will write a rock paper scissors game in class - Complete it in this file
import random
win = "You win!"
lose = "You lose."

# Function that retrieves the choices
def get_choices():
    player_choice = input("Enter choice: ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}

    return choices

def evaluation(choices:dict):
    player = choices["player"]
    com = choices["computer"]
    if player == com: print("Tie")
    elif player == "rock":
        if com == "paper": print(lose)
        elif com == "scissors": print(win)
    elif player == "paper":
        if com == "rock": print(win)
        elif com == "scissors": print(lose)
    elif player == 'scissors':
        if com == "rock": print(lose)
        elif com == "scissors": print(win)
        
while(1 == 1):    
    output = get_choices()
    if output["player"] == "exit": break
    evaluation(output)
