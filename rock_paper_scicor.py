import random
from colorama import init, Fore, Style

o= ["rock","paper","scissor "]

computer = o[random.randint(0,2)]

player = False

while player == False:
    player = input("Rock,Paper,Scissor")
    if player == computer:
        print("It's a Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!")
        else:
            print("You Win!")
    elif player == "Paper":
        if computer == "Scissor":
            print("You Lose!")
        else:
            Print("You Win!")
    elif player == "Scissor":
        if computer == "Rock":
            print("You lose!")
        else:
            print("You Win!")
    else:
        print("It's not a Valid input")
        