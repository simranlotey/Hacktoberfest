import random


# Function to simulate rolling a six-sided dice
def roll_dice():
    return random.randint(1, 6)


if __name__ == "__main__":
    # Prompt the user to roll the dice
    while True:
        user_input = input("Press Enter to roll the dice (q to quit): ")

        if user_input.lower() == 'q':
            break

        result = roll_dice()
        print(f"You rolled a {result}")
