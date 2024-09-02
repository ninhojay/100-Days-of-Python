import random
print("Welcome to the rock, paper and scissors game!")
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
picture= [rock, paper, scissors]
user_option= int(input("Enter 0 for rock, 1 for paper and 2 for scissors: \n"))
print(picture[user_option])

computer_option= random.randint(0,2)
print(f"computer chose: {computer_option}")
print(picture[user_option])

if user_option >= 3 or user_option < 0:
    print("You entered a wrong character, you lose")
elif user_option== 0 and computer_option== 1:
    print("You lose")
elif computer_option==0 and user_option==2:
    print("You lose")
elif user_option==1 and computer_option==2:
    print("You win!")
elif user_option== 2 and computer_option== 1:
    print("You win!")
elif computer_option== 0 and user_option==0:
    print("Its a draw!")
elif computer_option > user_option:
    print("You lose")
elif computer_option== user_option:
    print("Its a draw")

