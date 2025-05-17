import random

print("🎲 Welcome to the Dice Rolling Game 🎲")

while True:
    choice = input("Roll the dice? (y/n): ").lower()

    if choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"You rolled: ({die1}, {die2})\n")
    elif choice == 'n':
        print("Thanks for playing! 👋")
        break
    else:
        print("❌ Invalid choice! Please enter 'y' or 'n'.\n")
