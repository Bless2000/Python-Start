print("Hy my name is ")
 
name = "Blessed"
print ("Hy my name is " + name)

List = ['apple', 'banana', 'watermelon']
print(List)

List.append("orange")

List1 = ["shirt", "shorts", "trousers", "skirt"]
List1.insert(3, "jacket")
print(List1)

List.extend(List1)

List1.remove("shorts")
print(List1)

#Remove a specific index
List.pop(2)

print(List)

#Romoving the last item
List.pop()
print(List)

#delete the list completely
List2 = ["shirt", "shorts", "trousers", "skirt"]
#del List2

List2.clear()
print(List2)

#Loop through a List
for x in List:
    print(x)

#Looping through the indexes or index numbers
for i in range(len(List)):
    print(List[i])

#While Loop
i = 0
while i > len(List1):
    print(List1[i])
    i = i + 1

#Looping using List Comprehension (Short-Hand for writing loops)

[print(t) for t in List1]

#Sorting
List.sort()
print(List)

#Sorting list numerically
thislist = [1, 50, 62, 34, 71, 100]
thislist.sort()
print(thislist)

#Sorting descending other
List1.sort(reverse = True)
print(List1)


dictionary = {
    "name": "Blessed",
    "age": "14",
    "height": "6'2"
}
print(dictionary)

