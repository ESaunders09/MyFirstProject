import random

# Define characters that can be in the password
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&()_+-="
all_chars = letters + numbers + symbols # Combine everything

# Ask the user how long they want the password
length = int(input("How long do you want your password to be?"))
print("Password length set to:", length)

# Generate the random password
password = ""
for i in range(length):
    password += random.choice(all_chars)
print("Your password is:", password)