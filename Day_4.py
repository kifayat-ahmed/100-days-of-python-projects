#day 4 
# Rock paper scissors game
import random
rock=''' _______
      ---'   ____)
            (_____)
            (_____)
    VK      (____)
      ---.__(___)'''

paper = ''' _______
      ---'   ____)____
                ______)
                _______)
    VK         _______)
      ---.__________) '''

scissors = '''_______
      ---'   ____)____
                ______)
             __________)
    VK      (____)
      ---.__(___)'''

images =[rock,paper,scissors]

user_choice = int(input("Welcome to the game!,choose 0 for rock,1 for paper, 2 for scissors "))

computer_choice = random.randint(0,2)
 



if user_choice >= 3 or user_choice < 0:
    print("It is an invalid number,You lose!")
elif user_choice == computer_choice:
    print(images[user_choice])

    print(f"Computer chose {computer_choice}\n\n")
    print(images[computer_choice])
    print("its a draw\n")
    
elif computer_choice == 0 and user_choice == 2:
    print(images[user_choice])

    print(f"Computer chose {computer_choice}\n\n")
    print(images[computer_choice])
    print("You win!\n")
elif computer_choice == 2 and user_choice == 0:
    print(images[user_choice])

    print(f"Computer chose {computer_choice}\n\n")
    print(images[computer_choice])
    print("You lose!\n")
elif computer_choice > user_choice:
    print(images[user_choice])

    print(f"Computer chose {computer_choice}\n\n")
    print(images[computer_choice])
    print("You lose!\n")
elif computer_choice < user_choice:
    print(images[user_choice])

    print(f"Computer chose {computer_choice}\n\n")
    print(images[computer_choice])
    print("You win!\n")