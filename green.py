
year1 = [] 
year2 = [] 
months = ["Jan","Feb","Mar","Apr","May","Jun","jul","aug","sep","Oct","Nov","Dec"]
while True:
        print("year 1")
        year1 = [float(input("how many bottles today?: ")) for b in range(12)]
        print("year 2")
        year2 = [float(input("how many bottles today?: ")) for b in range(12)]
        
        
        savings = list()
        for list1, list2 in zip(year1, year2):
            savings.append(list1 - list2)
  
  
        option = str(input('would you like to contiune? yes or quit '))
        for letter in option:
             if letter in "n,N,q,Q":
                    quit("quit")
