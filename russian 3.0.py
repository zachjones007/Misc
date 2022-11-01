
#v3.0
import random # imports random
import turtle
x=input('hello for what we are doing next we need a name..so your willng to disclose you name?? Then what is it..')
whats_your_name=f'{x}' 
print(whats_your_name)
def name_gets_number():
    x =("hello {x} have you heard about russian rullet?? NO?! well ill tell you")
print ("....")
print ("the practice of loading a bullet into one chamber of a revolver, spinning the cylinder, and then pulling the trigger while pointing the gun at one's own head, care to play??.")
print('would you like to sign the waiver?')
print("SIGN WAIVER,print 'no' if you would like to exit:")
def translate(phrase):
    translation =""
    for letter in phrase:
        if letter in "no,nah,ni,yeah,yah":
            translation =   "... oh so you said yes?"
        
        else:
            quit()
    return translation
print(translate(input("yes or no, choose... NOW:")))
user_choice = input("1,2,3,4,5, or 6")
random_num = random.randint(1,6)
print ("russian rullett")
#cpu's choice
if random_num == 1:
    cpu_choice = '1st shot '
if random_num == 2:
    cpu_choice = ' 2nd shot'
if random_num == 3: 
    cpu_choice = ' 3rd choice' 
if random_num == 4:
    cpu_choice = '1st shot '
if random_num == 5:
    cpu_choice = ' 2nd shot'
if random_num == 6: 
    cpu_choice = ' 3rd choice' 
#player choice
if user_choice == 1:
    print = ('1st shot ')
if user_choice == 2:
    print = (' 2nd shot')
if user_choice == 3: 
    print = (' 3rd choice') 
if user_choice == 4:
    print = ('4st shot ')
if user_choice == 5:
    print = (' 5nd shot')
if user_choice == 6: 
    print (' 6rd choice')
print()
print("your choice:",user_choice )
print("computer choice:",cpu_choice )
print()
#1
if cpu_choice == ("2,3,4,5,6"):
        print("you live to see another round")  
elif cpu_choice == "1":
     print ("CLICK")
     quit()
#2
if cpu_choice == ("1,3,4,5,6"):
        print("you live to see another round")  
elif cpu_choice == "2":
     print ("CLICK")
     quit()
#3
if cpu_choice == ("2,1,4,5,6"):
        print("you live to see another round")  
elif cpu_choice == "3":
     print ("CLICK")
     quit()
#4
if cpu_choice == ("2,3,1,5,6"):
        print("you live to see another round")  
elif cpu_choice == "4":
     print ("CLICK")
     quit()
#5
if cpu_choice == ("2,3,4,6,1"):
        print("you live to see another round")  
elif cpu_choice == "5":
     print ("CLICK")
     quit()
#6
if cpu_choice == ("2,3,4,5,1"):
        print("you live to see another round")  
elif cpu_choice == "6":
     print ("CLICK")
     quit()
#no input 
if cpu_choice == (" "):
    quit()
print()
print("your choice:",user_choice )
print("computer choice:",cpu_choice )
print(whats_your_name)
print("you Survived, this round..")
sc = turtle.Screen()
sc.title("russian roulette")
sc.bgcolor("pink")
sc.setup(width=1000, height=600)
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)
#1
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
if cpu_choice == "1":
    left_pad.color("red")
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)
hit_ball = turtle.Turtle()
#2 
hit_ball.speed(40)
hit_ball.shape("circle")
if cpu_choice == "2":
    left_pad.color("red")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5
#3
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
if cpu_choice == "3":
    left_pad.color("red")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-200, -200)
#4
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
if cpu_choice == "4":
    left_pad.color("red")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-300, 200)
#5(red is the pad that is shot"red must take president over blue if user choice is selected")
left_pad = turtle.Turtle()
left_pad.speed(0)

left_pad.shape("square")
if cpu_choice == "5":
    left_pad.color("red")
left_pad.color("red")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(300, 200)
#6 (blue is the user choice"red must take president over blue if user choice is selected")
if random_num ('6'): 
    left_pad = turtle.Turtle()
    left_pad.speed(0)
    left_pad.shape("square")
    #if cpu_choice == "6" 
        #left_pad.color("red")
    left_pad.color("blue")
    left_pad.shapesize(stretch_wid=6, stretch_len=2)
    left_pad.penup()
    left_pad.goto(200, -200)