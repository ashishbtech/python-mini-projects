import random

print("Welcome to the Guessing Numbers Game")
print("Guess the number between 1 to 50 now!!")

secret_number = random.randint(1, 50)

attempts = 0   # counter for guesses

while True:

    guess_number = int(input("Guess the number: "))
    attempts += 1  #no. of attempts will increase as loop will repeat

    if guess_number > secret_number:
        print("Too High!!")

    elif guess_number < secret_number:
        print("Too Low!!")

    else:
        print("🎉 Congratulations! You guessed it right!")
        print("Number of attempts:", attempts)
        break