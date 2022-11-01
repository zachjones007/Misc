bottles = [] 
tax = float(.06)
total = 0

while True:
    order = int(input("do you want number 1, 2 or 3"))
    howmany = int(input('how many would you like? '))
    bottles.extend( [howmany] * howmany )
    
    if order == 1:
        total += howmany * .99
        option = input('would you like to quit? ')
        for letter in option:
                if letter in "yes,yeah,yah,quit":
                    quit("quittting")
    
    elif order == 2:
        total += howmany * .79
        option = input('would you like to quit? ')
        for letter in option:
                if letter in "yes,yeah,yah,quit":
                    quit("quittting")

    elif order == 3:
        total += howmany * 1.09
        option = input('would you like to quit? ')
        for letter in option:
                if letter in "yes,yeah,yah,quit":
                    quit("quittting")



    print( "Your otal after tax is :", total * (1+tax))
    
      





