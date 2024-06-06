# write 'hello world' to the console
# print('hello world') 
# Run the file with `python app.py`, it will display 'hello world'

import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'Tie'
    if (user_choice == 'Rock' and computer_choice == 'Scissors') or \
       (user_choice == 'Scissors' and computer_choice == 'Paper') or \
       (user_choice == 'Paper' and computer_choice == 'Rock'):
        return 'User wins'
    else:
        return 'Computer wins'
def play_game():
    choices = ['rock', 'paper', 'scissors']
    player_score = 0
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue
        computer_choice = random.choice(choices)
        print(f"Computer chose {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if result == 'User wins':
            player_score += 1
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break
    print(f"Player score: {player_score}")

play_game()
