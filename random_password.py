import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*"

all_characters = letters + numbers + symbols

length = int(input("Enter password length: "))

password = ""

for i in range(length):
    char = random.choice(all_characters)
    password += char

print("Generated Password:", password)