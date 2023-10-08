import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Set the initial number of guesses
    num_guesses = 0
    
    print("Welcome to Guess the Number!")
    print("I've selected a random number between 1 and 100. Try to guess it.")

    while True:
        try:
            # Get the player's guess
            guess = int(input("Enter your guess: "))
            num_guesses += 1

            # Check if the guess is correct
            if guess == secret_number:
                print(f"Congratulations! You've guessed the number {secret_number} in {num_guesses} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
