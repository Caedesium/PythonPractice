#!/usr/bin/env python3

# Rock, paper, scissors!

import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Please enter rock, paper, or scissors: ").lower()

    if user_choice in choices:
        cpu_choice = random.choice(choices)

        print(f"You chose: {user_choice}")
        print(f"CPU chose: {cpu_choice}")

        if user_choice == cpu_choice:
            print("You both chose the same thing! Try again.")
        elif (
            (user_choice == "rock" and cpu_choice == "scissors") or
            (user_choice == "paper" and cpu_choice == "rock") or
            (user_choice == "scissors" and cpu_choice == "paper")
        ):
            print("You won!")
        else:
            print("You lost...")
    else:
        print("Invalid choice. Please try again.")

play_game()