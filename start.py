import os
os.system('clear')

#############################################
### Data Types
# Strings
# Numbers
# List
# Tuples
# Dictionairies
# Boolean
#############################################


#Variables
#first_name = "Blessed"
#print(first_name)

#first_name = "bob"
#print(first_name)

#last_name = "Amponsah"

#first_name = last_name
#print(first_name)

#String
#first_name = "bob"

#Number
#Age = 41

#List 
#names = ['John', 'Bob', 'Mary']

#print(names)

#Tuples
#objects = ('box', 'chair', 'spoon')
#print(objects)

#Dictionary
#fav_pizza = {
#    'John': 'Pepperoni',
#    'Bob': 'Mushroom',
#    'Mary': 'Cheese'
#}
#print(fav_pizza['John'])
#print(fav_pizza)

#greetings = 'My Boss Yelled \"GET BACK TO WORK!\"'
#print(greetings)

##The Backticks are called escape charactares

#Concatination

#name = 'Bless'
#greet = "Hello my name is  " + name
#print(greet)

#age = "14"
#occ = 'student'

#intro = "Hello my name is " + name + ". I'm " + age + "years old. I'm a " + occ

#print(intro.title())
#print(intro.swapcase())
#print(len(intro)) 
#print(intro[20])
#print(intro[18:22])
#print(intro. split(" "))

##########NUmbers###################
#num = 10.25
#print(num)
#print(float(num))
#print(int(num))
########################################

########### List ##########################
#other_list = [1, 2, 3, 4, 5]
#other_name = 'Jerry'
#names = ["John", "Bob", "Tina", other_name, other_list]



#names.append("West")

#print(names)
#print(len((names)))
#print(names[len(names)-1])


#print(names[0])

#print(names[4])
#print(names[4][3])
#print(names[4][3] + 5)

#names.append(40)
#print(names)
#print(names[4] + 5)

#### Checking if an item is in the list ##################
thislist = ["apple", "lemon", "cherry", "pineapple"]
if "apple" in thislist:
    print("Yes, apple is in the list.")

###### List Ranges #########################################
thislist = ["apple", "lemon", "cherry", "pineapple"]
print(thislist[1:4])
print(thislist[2:])
print(thislist[:-1])


######### Range of Negative indexes###############
thislist = ["apple", "lemon", "cherry", "pineapple"]
print(thislist[-4:-1])

########## Changing the item value #####################################
thislist[1] = "Banana"
thislist[3] = "mango"
print(thislist)

####### Changing a range of item values ################################
thislist[2:4] = ["water", "blueberry"] 
print(thislist)

##If you insert less items than you replace, the new items will be inserted where you specifird, amd the remaining items will move accordingly.

##### Inserting Items #######################################################################

List1 = ["apple", "banana", "orange", "pineapple"]
List1.insert(2,"watermelon")
print(List1)


########### Extend List ###########################################################################
#To append elements from another list to the current list, use the extend() method.
List1.extend(thislist)
print(List1)


########################## List##################

############ Tuples ############################

#name_2 = ("John", "Bob", "Tina")
#tuple1 = ("Mary",)
#tuple2 = name_2 + tuple1
#print(tuple2[1:2])

#print(name_2)
#print(name_2[1])
############ Tuple ######################################

name_2 = ("John", "Bob", "Tina")
print(list(name_2))
print(tuple(name_2))


############# Dictionaries ########################

favorite_pizz = {
    "John": "Pepperoni",
    "Tim": "Sausage",
    "Mary": "Cheese"
}
print(favorite_pizz)
print(favorite_pizz["John"])
#del favorite_pizz["John"]

#print(favorite_pizz)

favorite_pizz.update({"Tina": "Green Peppers"})
print(favorite_pizz)

favorite_pizz["John"] = "Green Peppers"
print(favorite_pizz)


