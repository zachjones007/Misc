def main():   
    storeAmount1 = 0 
    storeAmount = 0
    user_choice = 0 
    user_choice1 = 0
    bonuspoints = 0 
    def part1():
        user_choice = input("months profit?'")
        how_many=f'profit: {user_choice}' 
        user_choice = int(user_choice)
        bonuspoints = f'congrats you got the max'
        if user_choice >= 110000 :
            storeAmount = 6000
        elif user_choice >=100000:
            storeAmount = 5000
        elif user_choice >=90000:
            storeAmount = 4000
        elif user_choice >=80000:
            storeAmount = 3000
        else:
            user_choice = 0
            storeAmount = 0
            part1()
    def part2():
        user_choice1 = input("monthly percent change?'")
        how_many1=f'change: {user_choice1}' 
        user_choice1 = int(user_choice1)
        if user_choice1 ==3:
            storeAmount1 = 40
        elif user_choice1 ==4:
            storeAmount1 = 50
        elif user_choice1 >= 5:
            storeAmount1 = 75
        else:
            user_choice1 <= 2.9
            storeAmount1 = 0
        print (user_choice,user_choice1,storeAmount,storeAmount1)
    part2()


    if storeAmount * storeAmount1 == 450000:
            print(bonuspoints)
main()