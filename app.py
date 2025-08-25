  # Treasurey project
    

rt random
def play_game():
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
                events = [
                    "You enter a room full of snakes. Game Over.",
                    "A fire starts suddenly! Game Over.",
                    "The door was locked. You waste time and lose. Game Over."
                ]
                print(random.choice(events))

            elif choice3 == "yellow": 
                events = [
                    "You found the Treasure! 🎉 You Win!",
                    "You opened the chest of gold! 🏆 You Win!",
                    "You discovered the lost crown! 👑 You Win!"
                ]
                print(random.choice(events))

            elif choice3 == "blue":
                events = [
                    "You enter a room full of lions. Game Over.",
                    "The floor collapses beneath you. Game Over.",
                    "You fall into a bottomless pit. Game Over."
                ]
                print(random.choice(events))

            else:
                print("You chose a door that doesn't exist. Game Over.")

        elif choice2 == "swim":
            events = [
                "You got attacked by a wolf. Game Over.",
                "A giant fish eats you. Game Over.",
                "You drown before reaching the island. Game Over."
            ]
            print(random.choice(events))

        else:
            print("Invalid choice. Game Over.")

    elif choice1 == "right":
        events = [
            "You fell into a hole. Game Over.",
            "You tripped on a rock and broke your leg. Game Over.",
            "A landslide buries the path. Game Over."
        ]
        print(random.choice(events))

    else:
        print("Invalid choice. Game Over.")


# Main game loop
while True:
    play_game()  # run the game once
    play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
    if play_again == "yes":
        continue  # restart game
    elif play_again == "no":
        print("Thanks for playing! Goodbye 👋")
        break
    else:
        print("Invalid input. Exiting the game.")
        break
