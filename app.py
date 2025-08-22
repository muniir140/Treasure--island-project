  # Treasurey project
    
print("Welcome to the Treasure Island")
print("Your mission is to find the Treasure")

choice1 = input("You're at a crossroad. Where do you want to go? Type 'right' or 'left': ").lower()

if choice1 == "left":
    choice2 = input("You have come to a lake. There is an island in the middle of the lake. "
                    "Type 'wait' to wait for a boat or 'swim' to swim across: ").lower()

    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors: "
                        "one red, one yellow, one blue. Which colour do you choose? ").lower()

        if choice3 == "red":
            print("You enter a room full of snakes. Game Over.")
        elif choice3 == "yellow":
            print("You found the Treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room full of lions. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by a wolf. Game Over.")

else:
    print("You fell into a hole. Game Over.")
