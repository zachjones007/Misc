import random
test_list = [ 'yes', 'no']
# guessing list
print("Original list is : " + str(test_list))
cpu_choice =[]
cpu_choice=("Random element is :", random.sample(test_list, 1)) 
number=(len(cpu_choice))
print(number)


if 4 <= len(cpu_choice):
  print (number)
x = 0
y = 0
match = False 
while x < 5 and y < number:

    userinput = input('guess a letter: ')[0]
    

    for letter in cpu_choice[1][0]:
      if letter != userinput:
        x = x +1 
        print("incorrect")
    for letter in cpu_choice[1][0]:
      if letter == userinput:
        match = True
        y = y +1 
        print("correct")

      
    print(cpu_choice)
    if number == y:
        print('you win')
        exit()

        
     

    
