'''
        create any small game for practice between user and  computer.
                use v5.10;

'''

import random
def get_computer_choice():
    choices = ['stone', 'paper', 'scissor']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == 'stone' and computer_choice == 'scissor') or \
         (user_choice == 'paper' and computer_choice == 'stone') or \
         (user_choice == 'scissor' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_choice = input("Enter your choice (stone, paper, scissor): ")
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

def main():
    while True:
        play_game()
        again = input("Do you want to play again? (y/yes or n/no): ").strip().lower()
        if again in ['n', 'no']:
            print("Thanks for playing!")
            break
        elif again in ['y', 'yes']:
            continue
        else:
            print("Invalid input, exiting game.")
            break

main()