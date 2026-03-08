import random

words = ["python", "apple", "tiger", "robot"]

secret_word = random.choice(words)

guessed_word = ["_"] * len(secret_word)

attempts = 6

print("Welcome to Hangman!")

while attempts > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))

    guess = input("Guess a letter: ").lower()

    if guess in secret_word:

        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess

    else:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

if "_" not in guessed_word:
    print("\n🎉 You guessed the word:", secret_word)
else:
    print("\n💀 Game Over! The word was:", secret_word)


