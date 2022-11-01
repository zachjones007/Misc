##Zach jones 12140 CIS129 Prog & Problem Solv I cookies extra credit 
#how many cookies would you like 1-40?
# if user chooses zero or less tell them to pick a number
#if the user chooses more then 40 tell them to pick a smaller number 
# multiply user choice by 75 to get calories 
# divide user choice by 4 to get serving amount 

user_choice = input("how many cookies would you like? '1-40'")
how_many=f'User Input: {user_choice}' 
print(how_many)
user_choice = int(user_choice)

if user_choice <=0:
  
  
  quit("pick a number")

if user_choice >=41:
  
  
  quit("pick a smaller number")
  

if user_choice ==1:
  
  print("just one cookie? thats only 75 calories")
  print ("servings",int(user_choice/4))
  quit

else:
  print ("calories",int(user_choice*75))
  print (int(user_choice/4),"servings",)
  quit

