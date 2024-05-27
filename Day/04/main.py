import random

# Define the representations for rock, paper, and scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
choices_names = ['Rock', 'Paper', 'Scissors']

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

if player_choice < 0 or player_choice > 2:
    print("Invalid input! Please enter 0, 1, or 2.")
else:
    print(f"You chose {choices_names[player_choice]}")
    print(choices[player_choice])

    computer_choice = random.randint(0, 2)

    print(f"Computer chose {choices_names[computer_choice]}")
    print(choices[computer_choice])

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice == 0) or (
            player_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("Computer wins!")
