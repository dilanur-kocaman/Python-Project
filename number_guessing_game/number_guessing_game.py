import random
from art import logo

easy_level = 10
hard_level = 5

#Function to check user's guess against actual answer.
def check_answer(guess, number, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > number:
    print("Too high.")
    return turns - 1
  elif guess < number:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {number}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return easy_level
  else:
    return hard_level

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  number = random.randint(1, 100)

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != number:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, number, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != number:
      print("Guess again.")

game()