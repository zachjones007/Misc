#zach jonyeses 
# 10-03-22
#

#Establishing bottles is a list 
bottles = [] 

while True:

    
      bottles = [float(input("how many bottles today?: ")) for _ in range(7)]
     # Multiply each value in bottle by 0.1 & print the sum
      print(sum([(b*0.1) for b in bottles]))
      option = str(input('would you like to contiune? yes or quit '))
      for letter in option:
                if letter in "n,N,q,Q":
                    quit("quittting")

    
   
    
      





