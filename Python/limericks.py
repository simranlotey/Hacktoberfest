#program to generate random limericks.
#In this program defines three functions: 1)generate_line_a() generates a random line for the A parts of the limerick. 2)generate_line_b() generates a random line for the B parts of the limerick. 3)generate_limerick() puts together the complete limerick with random lines for A and B parts.

import random

def generate_line_a():
    return random.choice(["There once was a cat", "A mouse ran so fast", "In a land far away", "A clever young rat", "Once a dog named Max"])

def generate_line_b():
    return random.choice(["In a hat full of cheese", "With a tail that would twitch", "That loved to chase mice", "With a plan, oh so slick", "Whose bark had a pitch"])

def generate_limerick():
    line_a1 = generate_line_a()
    line_a2 = generate_line_a()
    line_b1 = generate_line_b()
    line_b2 = generate_line_b()
    line_a3 = generate_line_a()

    limerick = f"{line_a1}\n{line_a2}\n{line_b1}\n{line_b2}\n{line_a3}"
    return limerick

if __name__ == "__main__":
    limerick = generate_limerick()
    print("Random Limerick:")
    print(limerick)
