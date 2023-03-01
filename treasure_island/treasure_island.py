from ascii_art import ascii

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("You\'re at a cross road. Where do you want to go? Type left or right.\n").lower()

if direction == "left":
    lake = input("You come to a lake. Type wait to wait for a boat or type swim.\n").lower()

    if lake == "wait":
        door = input("You arrive. there is three door. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        
        if door == "red":
            print("Burned by fire. Game Over.")
        elif door == "blue":
            print("Eaten by beasts. Game Over.")
        elif door == "yellow":
            print("You Win!")
        else:
            print("Game Over.")
    
    else:
        print("Attacked by trout. Game Over.")

else:
    print("You fall into a hole. Game Over.")