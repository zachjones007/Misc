
#The program should validate the numbers that are entered for each section
#A seats cost $20 each, section B seats cost $15 each, and section C seats cost $10 each.
# A seats cost $20 each, section B seats cost $15 each, and section C seats cost $10 each.
#  The theater has 300 seats in section A, 500 seats in section B,
#  and 200 seats in section C The theater has 300 seats in section A, 
# 500 seats in section B, and 200 seats in section C

def main():
    A = 300
    B = 500 
    C = 200
    




    #input number of seats sold for each class.
    remainderA = float(input('Enter total tickets sold for Class "A": '))
    remainderB= float(input('Enter total tickets sold for Class "B": '))
    remainderC = float(input('Enter total tickets sold for Class "C": '))
    
    def remainder():
            remaindera = float(remainderA - A)
            remainderb =float(remainderB - B) 
            remainderc = float(remainderC - C)
            def profit():
                fileda = (remaindera + 300)
                filedb = (remaindera + 500)
                filedc = (remaindera + 200)
                #print(profita)#,profitb, profitc)
                print(fileda)
            profit()
            
           
    remainder()

main()

