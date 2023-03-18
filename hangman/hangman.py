import random

from art import stages, logo
from words import word_list

print(logo)
print("Welcome to Hangman")

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False

lives = 6

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game: 
    guess_word = input("Guess a letter: ").lower()

    if guess_word in display:
        print(f"You have already guessed {guess_word}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess_word:
            display[position] = letter
    
    if guess_word not in chosen_word:
        print(f"You guessed {guess_word}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win!")

    print(stages[lives])










