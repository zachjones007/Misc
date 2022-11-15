#The program should validate the numbers that are entered for each section
#A seats cost $20 each, section B seats cost $15 each, and section C seats cost $10 each.
# A seats cost $20 each, section B seats cost $15 each, and section C seats cost $10 each.
#  The theater has 300 seats in section A, 500 seats in section B,
#  and 200 seats in section C The theater has 300 seats in section A, 
# 500 seats in section B, and 200 seats in section C

def main():
    #input number of seats sold for each class.
    remainderA = float(input('Enter total tickets sold for Class "A": '))
    remainderB= float(input('Enter total tickets sold for Class "B": '))
    remainderC = float(input('Enter total tickets sold for Class "C": '))
   
    def remainder(A,B,C):
            remaindera = float(remainderA - A)
            remainderb =float(remainderB - B) 
            remainderc = float(remainderC - C)
            def profit(priceA,priceB,priceC):
                fileda = (remaindera + A)
                filedb = (remainderb + B)
                filedc = (remainderc + C)
                #print(profita)#,profitb, profitc)
            
                a = int(fileda*priceA)
                b = int(filedb*priceB)
                c = int(filedc*priceC)

                print ("seats left in Section A",int(-remaindera))
                print ("seats left in Section B",int(-remainderb))
                print ("seats left in Section C",int(-remainderc))
                print ("Section A profit :",a,"$","Section B profit :",b,"$","Section C profit :",c,"$")
               
                print("total profit:",int((a)+(b)+(b)),"$")
            profit(20,15,10)
                    
    remainder(300,500,200)
main()