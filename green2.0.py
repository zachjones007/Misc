
year1 = [] 
year2 = [] 
months = ["Jan","Feb","Mar","Apr","May","Jun","jul","aug","sep","Oct","Nov","Dec"]

while True:
    for i in range( len(months)):
        print("how many bottles in : ", months[i], "for year 1")
        year1.append(int(input()))
        print("how many bottles in : ", months[i], "for year 2")
        year2.append(int(input()))
       

        savings = list()
        for list1, list2 in zip(year1, year2):
            savings.append(list1 - list2)
   
    res = "\n".join("{} {}".format(x, y) for x, y in zip(savings, months))
    print(res)
        


    option = str(input('would you like to contiune? yes or quit '))
    for letter in option:
             if letter in "n,N,q,Q":
                    quit("quit")
