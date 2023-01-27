#Rock Paper Scissor game
import random
# Rock Paper Scissors ASCII Art

# Rock
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Paper
paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# Scissors
scissor='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

image=[rock,paper,scissor]

print("Welcome to Rock-Paper-Scissor game!\n")
usr_choice = input("What do you choose? Press 0 for 'Rock', 1 for 'Paper' or 2 for 'Scissor': ")

user_choice=int(usr_choice)
comp_choice = random.randint(0,2)

print (f"\nYour choice:\n{image[user_choice]}\n")
print (f"\nComputer choice\n{image[comp_choice]}")

if (user_choice==0 and comp_choice==2):
  print(f"You won! Computer chose {comp_choice} and you {user_choice}")
elif (user_choice==2 and comp_choice==0):
  print(f"You lose! Computer chose {comp_choice} and you {user_choice}")
elif (user_choice<comp_choice):
  print(f"You lose! Computer chose {comp_choice} and you {user_choice}")
elif(user_choice>comp_choice):
  print(f"You won! Computer chose {comp_choice} and you {user_choice}")
elif(user_choice==comp_choice):
  print(f"You draw! Computer chose {comp_choice} and you {user_choice}")
else:
  print("You insert a wrong number!")

