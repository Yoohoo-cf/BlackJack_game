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


import random

user_choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))

if user_choice not in [0, 1, 2]:
    print("You typed an invalid number. You lose!")

computer_choice = random.randint(0, 2)
print(f"Computer chose: {computer_choice}\n")


if user_choice == 0 and computer_choice == 2:
    print(f"You chose {rock}\nComputer chose {scissors}. You win!")
elif user_choice == 2 and computer_choice == 1:
    print(f"You chose {scissors}\nComputer chose {paper}. You win!")
elif user_choice == 1 and computer_choice == 0:
    print(f"You chose: {paper}\nComputer chose: {rock}. You win!")
elif user_choice == computer_choice:
    print("Tie")
else:
    print("Computer wins!")