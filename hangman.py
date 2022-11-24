import random
test_list = [ 'yes', 'no']
# guessing list
print("Original list is : " + str(test_list))
cpu_choice =[]
cpu_choice=("Random element is :", random.sample(test_list, 1)) 
number=(len(cpu_choice))


if 4 <= len(cpu_choice):
  print (number)
x = 0
y = 0
while x < 5:
 
  while y < number:
  #numbers = 2 
  
  
  
    userinput = input('guess a letter: ')[0]
    match = False
    for letter in cpu_choice[1][0]:
      if letter == userinput:
        match = True
        y = y +1 
        # add one to y to make it equal to len of cpu choice
        

        if len(cpu_choice) == y:
          quit('quit')
    if match:
      print('correct')
      y=y+1
    else:
      print('wrong')
      x = x + 1
print("end")

    
