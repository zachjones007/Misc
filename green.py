
year1 = []
year2 = []
months = ["Jan","Feb"]#,"Mar","Apr","May","Jun","jul","aug","sep","Oct","Nov","Dec"]
while True:
    for i in range( len(months)):
        print("Enter the number of green beans harvested in", months[i], "for year 1")
        year1.append(int(input()))
        print("Enter the number of green beans harvested in", months[i], "for year 2")
        year2.append(int(input()))
    print(year1)    
    print(year2)
        
        
    savings = list()
    for list1, list2 in zip(year1, year2):
            print(savings + months)

    print(*months, sep = "\n")
    break

#++++ 
#++++
#++++
#++++
#++++ 


sentence = "WHAT IS MINE IS YOURS AND WHAT IS YOURS IS MINE";

sentence = sentence.lower();

sentence = sentence.split();

uniqueWord = [];

store = [];

for i in sentence:
    if i not in uniqueWord:
        uniqueWord.append(i);

lengthOfUniqueWord = len(uniqueWord);

print(sentence);

print(uniqueWord);

for i in range(lengthOfUniqueWord):
    i = str(i+1);
    store.append(i);

print(store);

for positions in enumerate(uniqueWord, 1):
     print(positions);