import random # imports random

while True:
    username = input("player 1 name :")
    username1 = input("player 2 name :")
    user_choice = random.randint(1,6)
    user_choice1 = random.randint(1,6)
    
    

    print("your choice:",user_choice )
    print("computer choice:",user_choice1 )

    if user_choice <= user_choice1:

        print({username},"wins")  

        
        option = input('would you like to quit? ')
        for letter in option:
                if letter in "y,q,Y,Q":
                    quit("quittting")

    #no input 
    elif user_choice1 >= user_choice:
        print({username1}," wins")

        
        option = input('would you like to quit? ')
        for letter in option:
                if letter in "y,q,Y,Q":
                    quit("quitting")



