import game

while True:
    print("\n1. Play round")
    print("2. Show rules")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        game.play_round()
    elif choice == 2:
        game.show_rules()
    elif choice == 3:
        print("Thanks for playing!")
        break