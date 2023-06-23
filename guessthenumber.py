import random

def guess_the_number():
    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        guess_the_number()
    else:
        print("Thank you for playing!")

# Start the game
guess_the_number()

# 1. We start by importing the `random` module. This module allows us to generate random numbers in Python.

# 2. We define a function called `guess_the_number()` that encapsulates the logic of the game. Functions are reusable blocks of code that perform specific tasks.

# 3. Inside the `guess_the_number()` function, we generate a random number between 1 and 100 using `random.randint(1, 100)`. This number will be the target number that the player needs to guess.

# 4. We initialize a variable called `attempts` to keep track of the number of attempts the player has made.

# 5. We enter a `while True` loop, which means the following block of code will keep executing until we explicitly break out of the loop.

# 6. Inside the loop, we prompt the player to enter their guess by using `input("Guess the number (between 1 and 100): ")`. The `input()` function allows us to get user input from the keyboard.

# 7. We convert the user's input, which is initially a string, into an integer using `int(guess)`.

# 8. We increment the `attempts` variable by 1 to keep track of the number of attempts.

# 9. We check if the guess is less than the random number. If it is, we inform the player that their guess is too low and prompt them to try again.

# 10. If the guess is greater than the random number, we inform the player that their guess is too high and prompt them to try again.

# 11. If the guess matches the random number, we display a congratulatory message along with the number of attempts it took to guess correctly using `print(f"Congratulations! You guessed the number in {attempts} attempts.")`.

# 12. We use the `break` statement to exit the `while` loop once the correct number is guessed.

# 13. After the loop, we ask the player if they want to play again by using `input("Do you want to play again? (yes/no): ")`.

# 14. If the player responds with "yes" (regardless of the letter case), we recursively call the `guess_the_number()` function to start a new game.

# 15. If the player responds with "no" (regardless of the letter case), we print a farewell message and the program ends.

# 16. Finally, we start the game by calling the `guess_the_number()` function at the bottom of the code.
