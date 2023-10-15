import random
import string

def generate_random_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Use random.choice to generate a random password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    random_password = generate_random_password(password_length)
    print(f"Random Password: {random_password}")
