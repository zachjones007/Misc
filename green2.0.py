
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
    
    sentence = "WHAT IS MINE IS YOURS AND WHAT IS YOURS IS MINE";
    sentence = sentence.split();

    

    for i in sentence:
            if i not in savings:
                savings.append(i);

    for positions in enumerate(savings, 1):
        print(positions);

    
        


    option = str(input('would you like to contiune? yes or quit '))
    for letter in option:
             if letter in "n,N,q,Q":
                    quit("quit")