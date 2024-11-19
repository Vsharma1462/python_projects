# rules-1 rock wins against scissors
# rule -2 scissor wins against paper
# rule -3 paper wins against rock

#  1. rock -0
# 2. paper-1
# 3. scissor-2 

import random

rock='''@@@@@
        @@@@@
        @@@@@'''

paper='''####
         ####
         ####'''
scissor='''$$$$
           $$$$
           $$$$'''


game_images=[rock,paper,scissor]
             
user_input=int(input("enter choice :"))

if user_input>=3 or user_input<0:
    print("enter valid input")

else:
    print(game_images[user_input])
    computer_input=random.randint(0,2) 
    print(f"comp_input {computer_input}") 
    print(game_images[computer_input])  

    if user_input==computer_input:
        print("draw")

    elif computer_input == 0 and user_input==2:

        print("you loose")

    elif computer_input==2 and user_input==0:
        print("you won")
        print("computer losse")        

    elif computer_input>user_input:
        print("you loose")
        print("computer won")

    elif user_input>computer_input:

        print("you won")  
        print("computer loose")      
