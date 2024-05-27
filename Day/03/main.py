print("Welcome to Treasure Island. Your mission is to find the treasure.")

choice1 = input("You are at a cross road. Do you choose to go left or right? ")
if choice1 == "right":
    print("You fell into a trap hole. Game over")
elif choice1 == "left":
    choice2 = input("You are by the lake. Do you choose to swim or wait for the boat? ")
    if choice2 == "swim":
        print("Game over. You've been eaten by a bull shark.")
    if choice2 == "wait":
        choice3 = input("Which door do you choose to take? Blue, Red, or Yellow? ")
        if choice3 == "blue":
            print("Game over")
        if choice3 == "red":
            print("Game over")
        if choice3 == "yellow":
            print("You win!")