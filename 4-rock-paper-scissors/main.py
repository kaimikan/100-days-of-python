# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random

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

choices_strings = ['rock', 'paper', 'scissors']

choices_visuals = [rock, paper, scissors]
computer_choice = random.randint(0, 2)
your_choice = input("Rock, paper or scissors? ").lower()
your_choice_index = choices_strings.index(your_choice)

print(f"Computer chose {choices_strings[computer_choice]}\n",
      f"{choices_visuals[computer_choice]}\n\n",
      f"You chose {choices_strings[your_choice_index]}\n",
      f"{choices_visuals[your_choice_index]}")

rock_index = 0
paper_index = 1
scissors_index = 2
you_won = False
tie = False

if your_choice_index == rock_index:
    if computer_choice == scissors_index:
        you_won = True
elif your_choice_index == paper_index:
    if computer_choice == rock_index:
        you_won = True
elif your_choice_index == scissors_index:
    if computer_choice == paper_index:
        you_won = True

if your_choice_index == computer_choice:
    tie = True

if tie:
    print("\nYou Tied!")
elif you_won:
    print("\nYou Won!")
elif not you_won:
    print("\nYou Lost!")
