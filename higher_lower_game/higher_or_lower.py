import random
from art import logo, vs
from game_data import data
from replit import clear

def get_random_account():
    """Get data from random account"""
    return random.choice(data)

# Format the account data into printable format.
def format_data(account):
    """Format account into printable format: name, description and country"""
    account_name = account["name"]
    account_desc = account["description"]
    account_count = account["country"]
    return f"{account_name}, a {account_desc}, from {account_count}."

def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess and returns True if they got it right. Or False if they got it wrong.""" 
    if a_followers > b_followers:
        if guess == "a":
            return True
        else:
            return False
    else:
        return guess == "b"

def game():
    print(logo)
    score = 0
    account_a = get_random_account()
    account_b = get_random_account()

    # Make the game repeatable. 
    is_continue = True
    while is_continue:
        # Generate the random accounts from the game data.

        # Making account at position B become the next account at position A.
        account_a = account_b
        account_b = get_random_account()

        ## Account A and B must be different.
        while account_a == account_b:
            account_b = get_random_account()
            
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        # Ask user for a guess.
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Check if user is correct. 
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        clear()
        print(logo)

        # Give user feedback on their guess. 
        # Score keeping.
        if is_correct:
            score += 1
            print(f"You are right! Current score: {score}.")
        else:
            is_continue = False
            print(f"Sorry, that's wrong. Final score {score}.")

game()

















