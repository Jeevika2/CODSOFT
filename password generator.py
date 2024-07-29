import random
import string

print("Welcome to the Password Generator!")

# Prompt the user to specify the desired length of the password
while True:
    try:
        length = int(input("Enter the desired length for the password: "))
        if length <= 0:
            raise ValueError("Length should be a positive integer.")
        break
    except ValueError as ve:
        print(f"Invalid input: {ve}")

# Define the possible characters in the password
characters = string.ascii_letters + string.digits + string.punctuation

# Shuffle the characters to create randomness
shuffled_chars = random.sample(characters, len(characters))

# Generate a password of the specified length
password = ''.join(random.sample(shuffled_chars, length))

# Display the generated password
print(f"Generated Password: {password}")

