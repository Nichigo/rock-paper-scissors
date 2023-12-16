#!/usr/bin/env python3
# Rock, Paper, Scissors Game
# This is a simple rock, paper, scissors game that allows the user to play against the computer.
# The computer will randomly choose rock, paper, or scissors, and the user will be prompted for their choice.
# The game will then display the winner and the score.
# The user can quit the game at any time by typing "quit" at the prompt.

import random

def print_final_score(score, games_played):
    print("You played", games_played, "games and won", score, "of them.")
    print("Your win rate was", round(score / games_played * 100, 2), "%.")
    print("Thanks for playing!")
    print("Goodbye!")

print("Let's play Rock, Paper, Scissors!")
print("You can type rock, paper, or scissors at the prompt.")

user_score = 0
computer_score = 0
games_played = 0

options = ["rock", "paper", "scissors"]

while True:
    try:
        print("-------------------------------------")
        user_choice = input("Enter your choice (rock, paper, or scissors), or type 'quit' to exit: ")

        user_choice = user_choice.lower()

        if user_choice == "quit":
            print_final_score(user_score, games_played)
            break

        # If the user types "r" or "p" or "s", the program will assume they meant "rock" or "paper" or "scissors".
        for option in options:
            if option.startswith(user_choice):
                user_choice = option
                break

        if user_choice not in options:
            print("Invalid choice. Please try again.")
            continue
        
        games_played += 1
        computer_choice = random.choice(["rock", "paper", "scissors"])

        print("The computer chose", computer_choice + ".")

        if user_choice == computer_choice:
            print("It's a tie!")

        elif user_choice == "rock":
            if computer_choice == "paper":
                print("You lose!", computer_choice, "covers", user_choice)
                computer_score += 1
            else:
                print("You win!", user_choice, "smashes", computer_choice)
                user_score += 1
        elif user_choice == "paper":
            if computer_choice == "scissors":
                print("You lose!", computer_choice, "cut", user_choice)
                computer_score += 1
            else:
                print("You win!", user_choice, "covers", computer_choice)
                user_score += 1
        else:
            if computer_choice == "rock":
                print("You lose!", computer_choice, "smashes", user_choice)
                computer_score += 1
            else:
                print("You win!", user_choice, "cuts", computer_choice)
                user_score += 1

        print("User:", user_score, "Computer", computer_score, "Games Played:", games_played)
    except KeyboardInterrupt:
        print_final_score(user_score, games_played)
        break

