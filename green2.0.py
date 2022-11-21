#program that will allow the user to enter the energy
#bills from January to December for the year prior to going
#green. Next, allow the user to enter the energy bills
#from January to December of the past year after going
#green. The program should calculate the energy difference
#from the two years and display the two years worth of
#data, along with the savings.



year1 = [] 
year2 = [] 
months = ["Jan","Feb","Mar","Apr","May","Jun","jul","aug","sep","Oct","Nov","Dec"]

for i in range(len(months)):
        print("amount payed before going green : ", months[i], "for year 1")
        year1.append(float(input()))
        print("amount payed after going green : ", months[i], "for year 2")
        year2.append(float(input()))
       

        savings = list()
        for list1, list2 in zip(year1, year2):
            savings.append(list1 - list2)
   
res = "\n".join("the savings for {} since going green is {}$ ".format(x, y) for x, y in zip(months, savings))
print("your savings for going green per month are: ")
print(res)
        



