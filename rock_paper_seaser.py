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
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors ='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list = [rock,paper,scissors]
your_choice = int(input("Enter Your Choise  0 for rock , 1 for paper , 2 for scissors"))
computer_choice = random.randint(0,2)
if your_choice >=3 or your_choice < 0 :
    print("You Typeed Invaild number , You Losse")
else:

    if (your_choice == 0 and  computer_choice == 2 ) or (your_choice == 1 and computer_choice == 0) or (your_choice == 2 and computer_choice == 1) :
        print(f"Your Choice :  \n {list[your_choice]}")
        print(f"Computer  Choice : \n {list[computer_choice]}")
        print("So , You Won")
    elif (your_choice == 1 and computer_choice == 2) or (your_choice == 2 and computer_choice == 0) :
        print(f"Your Choice : \n {list[your_choice]}")
        print(f"Computer Choice : \n {list[computer_choice]}")
        print("So , You Loss")
    elif your_choice == computer_choice :
        print("It's A draw")
    else:
        print("You typed invaild Number , You Loss")

