import random
import os

def game():
    game_end = False

    while not game_end:
        print("Welcome to the number guessing game!")
        print("I'm thinking of a number between 1 and 100")
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        random_number = random.randrange(1,101)

        if difficulty == "easy":
            attempts = 10
        else:
            attempts = 5
        
        for _ in range(1, attempts+1):
            while attempts > 0:
                print(f"You have {attempts} guesses remaining.")
                guess = int(input("Make a guess: "))

                if guess > random_number:
                    print("Too high")
                elif guess < random_number:
                    print("Too low")
                elif guess == random_number:
                    print("You got it!")
                    attempts = 0
                    break

                attempts = attempts - 1
        
        if attempts == 0:
            print(f"the number was: {random_number}")
            game_end = True

        i = input("Do you want to play again? Type 'yes' or 'no': ")
        if i == "no":
            game_end = True
            break
        elif i == "yes":
            os.system("cls")
            game()


game()