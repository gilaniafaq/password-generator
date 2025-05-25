import random
import string

# Input password length
length = int(input("Enter the length of your password (min 4): "))

# Guarantee 1 character from each type
upper = random.choice(string.ascii_uppercase)
lower = random.choice(string.ascii_lowercase)
digit = random.choice(string.digits)
symbol = random.choice(string.punctuation)

# Fill the rest of the password with random characters
remaining_length = length - 4
all_chars = string.ascii_letters + string.digits + string.punctuation
remaining = random.choices(all_chars, k=remaining_length)

# Combine all parts and shuffle
password_list = [upper, lower, digit, symbol] + remaining
random.shuffle(password_list)
password = ''.join(password_list)

# Ask what the password is for
account_name = input("What is this password for? (e.g., Facebook, Gmail): ").title()

# Print and save
print(f"\nSucessfully generated password for {account_name}: {password}")

with open("passwords.txt", "a") as file:
    file.write(f"{account_name}: {password}\n")

print("Password saved to 'passwords.txt'.")
