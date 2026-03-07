import random

print("Think of a number between 1 and 100.")

low = 1
high = 100

while True:

    guess = random.randint(low, high)

    print(f"My guess is: {guess}")

    hint = input("Too High (h), Too Low (l), Correct (c)? ")

    if hint == 'h':
        high = guess - 1

    elif hint == 'l':
        low = guess + 1

    elif hint == 'c':
        print("Yay! I guessed your number!")
        break