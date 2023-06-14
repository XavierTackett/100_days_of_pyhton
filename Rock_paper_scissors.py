    # The rock, paper, scissors game 
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
images = [rock, paper, scissors]

print("Rock, Paper, Scissors game")
user_choice = int(input("Whats do you choose? Rock is 0, Paper is 1, and Scissors is 2. Please type in the number.\n"))
if user_choice >= 3 or user_choice <= 0:
  print("You typed an invalid number you lose ")
else:

  print(images[user_choice])
  
  computer_choice = random.randint(0, 2)
  print(f"Computer chose:")
  print(images[computer_choice]) 
  
  if user_choice >= 3 or user_choice <= 0:
    print("You typed an invalid number you lose ")
  elif user_choice == 0 and computer_choice == 2:
    print("You win!!")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose")
  elif computer_choice > user_choice:
    print("You lose")
  elif user_choice > computer_choice:
    print("You win !!")
  elif user_choice == computer_choice:
    print("It was a drawl go again")
