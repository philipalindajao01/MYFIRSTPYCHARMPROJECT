#COLLECTION
#list [ A, B, C, D]
#Dictionary (1A,: B, C, D)
#SET {A, B, C, D  }
#TUPLE (A, B, C, D)

#COLLECTION WITHIN COLLECTION
# LIST [[ABCD], [12345]]
# LIST MUTABLE ORDERED,DUPLICATE
#TUPLE UNMUTABLE, UNORDERED,
#SET MUTABLE NOT ORDERED NOT ALLOWING DUPLICATE

myList = ["apple", "banana", "cherry", "dalandan"]
myTuple = ("apple", "banana", "cherry", "dalandan")

myList.append("apple")
print(myList)

myList.insert(2, "chico")
print(myList)

print (myList[0]) #start
print (myList[4]) #dalandan
print (myList[len(myList)-1]) #end

print(myList.index("chico")) #to get index or postion no.
print(myList.count("chico")) #to get the count of
myList.remove("chico")
print(myList)

myStudents = [
    ["Name","Age", "City", "Year", "Section"],
    ["Philip Alindajao", "18", "Las Pinas ", "First", "Two"],
    ["Philip Charles", "18", "Las Pinas ", "Second", "Two"],
    ["Philip Charles Alindajao", "20", "Muntinlupa ", "First", "One"],
    ["Philip Charles Duron Alindajao", "18", "Las Pinas ", "First", "Two"]
] #List of List
print(myStudents[0].index("Year"))
print(myStudents[3])


