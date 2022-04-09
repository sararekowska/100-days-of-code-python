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

options = [rock, paper, scissors]

print("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors")
choice = int(input())
choice_computer = random.randint(0,2)

if choice == 1 or choice == 2 or choice == 0:
    print("You chose:")
    print(options[choice])
    print("Computer chose:")
    print(options[choice_computer])
    
    if choice == choice_computer:
        print("It's a draw!")
    elif choice == 0:
        if choice_computer == 1:
            print("You lose!")
        elif choice_computer == 2:
            print("You win!")
    elif choice == 1:
        if choice_computer == 0:
            print("You win!")
        elif choice_computer == 2:
            print("You lose!")
    elif choice == 2:
        if choice_computer == 0:
            print("You lose!")
        elif choice_computer == 1:
            print("You win!")

else:
    print("You typed an incorrect number, game over!")

