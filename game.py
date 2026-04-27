import random

choices = ["stone", "paper", "scissors"]

def get_computer_choice():
    return random.choice(choices)

def get_winner(player, computer):
    if player == computer:
        return "tie"
    if (player == "stone" and computer == "scissors") or \
       (player == "paper" and computer == "stone") or \
       (player == "scissors" and computer == "paper"):
        return "player"
    return "computer"

def play_round():
    print("\n1. Stone  2. Paper  3. Scissors")
    choice = int(input("Enter your choice: "))
    if choice not in [1, 2, 3]:
        print("Invalid choice.")
        return

    player = choices[choice - 1]
    computer = get_computer_choice()
    print(f"You: {player} | Computer: {computer}")

    result = get_winner(player, computer)
    if result == "tie":
        print("It's a tie!")
    elif result == "player":
        print("You win!")
    else:
        print("Computer wins!")

def show_rules():
    print("Stone beats Scissors")
    print("Scissors beats Paper")
    print("Paper beats Stone")