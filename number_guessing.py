import random

secret = random.randint(1, 100)
attempts = 0

print("Guess a number from 1 to 100.")

while True:
    try:
        guess = int(input("Your guess: "))
    except ValueError:
        print("Enter a valid integer.")
        continue

    attempts += 1
    if guess < secret:
        print("Too low.")
    elif guess > secret:
        print("Too high.")
    else:
        print(f"Correct! Attempts: {attempts}")
        break
