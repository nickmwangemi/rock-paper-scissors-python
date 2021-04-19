import random


def computer_play():    
    possible_outcomes = ['rock', 'paper', 'scissors']
    return random.choice(possible_outcomes)


def game_play(user_input):
    if user_input == computer_play():
        print(f"Both players selected {user_input}. It's a tie!")
    elif user_input == "rock":
        if computer_play() == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_input == "paper":
        if computer_play() == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_input == "scissors":
        if computer_play() == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
