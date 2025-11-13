import random

def play_game():
    user_score = 0
    computer_score = 0

    print(" Welcome to the Rock-Paper-Scissors Game!")
    print("------------------------------------------------")

    while True:
        print("\nChoose one: rock, paper, or scissors")
        user_choice = input(" Your choice: ").lower()
        choices = ["rock", "paper", "scissors"]

        if user_choice not in choices:
            print(" Invalid choice! Please try again.")
            continue

        computer_choice = random.choice(choices)
        print(f" Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print(" It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win this round!")
            user_score += 1
        else:
            print(" Computer wins this round!")
            computer_score += 1

        print(f" Score -> You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing! Final Score:")
            print(f" You: {user_score} |  Computer: {computer_score}")
            break

play_game()
