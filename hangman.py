





import random
test_list = [ 'yes', 'no']
# guessing list
print("Original list is : " + str(test_list))
cpu_choice =[]
cpu_choice=("Random element is :", random.sample(test_list, 1)) 
number=(len(cpu_choice))
print(number)



x = 0
y = 0
match = False 

while x < 5:
  
  
  
  
    userinput = input('guess a letter: ')[0]
    match = False
    
    for letter in cpu_choice[1][0]:
      if letter == userinput:
        match = True
  
        
        if len(cpu_choice) == y:
          quit('quit')
    if match:
      print('correct')
      y=y+1
    else:
      print('wrong')
      x = x + 1
print("end")


#++++ top code x works bottom code y works
while x < 5:

    userinput = input('guess a letter: ')[0]
    if y < number:
      quit
    

  
      
    for letter in cpu_choice[1][0]:
      if letter == userinput:
        match = True
        y = y +1 
        print("correct")

      elif x + 1:
        print ('incorrect')
        match = False 
    print(cpu_choice)
    if number == y:
        print('you win')
        exit()

        
     

    
