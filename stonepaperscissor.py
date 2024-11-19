import random

rock = '''   
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
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

gameimage = [rock, paper, scissors]
print("Welcome to the game Rock, Paper, Scissors!")

user_choice = int(input("What do you want to choose? 0 for Rock, 1 for Paper, 2 for Scissors\n"))
if user_choice < 0 or user_choice > 2:
    print("Invalid input")
else:
    print(gameimage[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(gameimage[computer_choice])

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 1 and computer_choice == 0):
        print("You win!")
    else:
        print("Computer wins!")

"""Rock0 beats 2Scissors (🪨 > ✂️)

Scissors2 beat 1Paper (✂️ > 📄)

Paper 1 beats Rock 0 (📄 > 🪨)"""
