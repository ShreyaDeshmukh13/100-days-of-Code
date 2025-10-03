# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


import random
game_images = [rock, paper, scissors]
computer_choice = random.randint(0,2)
user_choice = int (input("What do you choose ?  Type 0 for rock , 1 for paper , 2 for scissors\n"))
print(game_images[user_choice])
print(f'computer choose :{ computer_choice }')
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0 :
    print("You typed an invalid number , you lose :( ")

elif user_choice == computer_choice:
    print("It's a Draw")

elif computer_choice == 0 and user_choice == 2:
    print("YOU LOSE")

elif computer_choice > user_choice:
    print("YOU LOSE")

elif computer_choice < user_choice:
    print("YOU WIN")

elif computer_choice == 0 and user_choice == 2:
    print("YOU LOSE")


