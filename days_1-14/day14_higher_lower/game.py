import art
from game_data import data
import random
import os

def random_account():
    return random.choice(data)

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description} from {country}"

def check_answer(guess, a, b):
    if a > b:
        return guess == "a"
    else:
        return guess == "b"

def game():
    print(art.logo)
    score = 0
    game_continue = True
    account_a = random_account()
    account_b = random_account()

    while game_continue:
        account_a = account_b
        account_b = random_account()

        while account_a == account_b:
            account_b = random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(art.vs)
        print(f"Against B: {format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        os.system('cls')
        print(art.logo)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

game()