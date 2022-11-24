import random
test_list = [ 'yes', 'no']
# guessing list
print("Original list is : " + str(test_list))
cpu_choice =[]
cpu_choice=("Random element is :", random.sample(test_list, 1)) 
print (cpu_choice) 

userinput = input('guess a letter: ')[0]
match = False
for letter in cpu_choice[1][0]:
  if letter == userinput:
    match = True
    break
if match:
  print('correct')
else:
  print('wrong')

