import random

def get_no_of_attempts():
    while True:
        difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty_level == 'hard':
            return 5
        elif difficulty_level == 'easy':
            return 10
        else:
            print("Invalid choice, Please type 'easy' or 'hard'")

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    actual_number = random.randint(1, 100)
    print(f"Actual number: {actual_number}")
    no_of_attempts = get_no_of_attempts()

    while no_of_attempts > 0:
        print(f"You have {no_of_attempts} attempts remaining to guess the number.") # repeated
        guess_number = int(input("Make a guess: ")) # repeated
        
        if guess_number == actual_number:
            print("Congratulations! You guessed the right number!")
            return
        elif guess_number < actual_number:
            print("Too low.")
        elif guess_number > actual_number:
            print("Too high.")

        no_of_attempts -= 1
        if no_of_attempts > 0:
            print("Guess again.")

    print(f"\nYou've run out of attempts. The number was {actual_number}.")

play_game()