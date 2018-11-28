# Lists
shopping_list = ["whole milk", "PC", "Eggs", "Xbox One"]
print(shopping_list)
print(shopping_list[0])
print("The second thing in the list is %s" % shopping_list[1])
print("The length of the list is %d" % len(shopping_list))

# Changing Elements in a list
shopping_list[0] = "2% milk"
print(shopping_list)
print(shopping_list[0])

# Looping through lists
for item in shopping_list:
    print(item)

'''
1. Make a list
2. change the 3rd thing in the list
3. print the item
4. print the full list
'''
new_list = ["eggs", "cheese", "oranges","raspberries","apples"]
new_list [2] = "oranges"
print("The last thing in the list is %s" % new_list[len(new_list) - 1])
print(new_list)

# Getting part of a list
print(new_list[1:3])
print(new_list[1:4])
print(new_list[1:])
print(new_list[:2])

#Adding things to a list
holiday_list = []  #ALWAYS USE SQUARE BRACKETS FOR LISTS
holiday_list.append("Tacos")
holiday_list.append("Bumblebee")
holiday_list.append("Red Dead Redemption 2")
print(holiday_list)

# Notice this is object.method(Parameter)"

# Removing things from a list
holiday_list.remove("Tacos")
print(holiday_list)


holiday_list = []
holiday_list.append("Math Book")
holiday_list.append("Women")
holiday_list.append("Dogs")
holiday_list.append("Computer")
print(holiday_list)

holiday_list.remove("Math Book")
print(holiday_list)

# ALSO removing things from a list
holiday_list.pop(0) #Removes the item at index 0
print(holiday_list)

#Tuble
brands = ("apple","Samsung","HTC") # notice the parenthesis

colors = ['blue', 'green','red','purple','cyan','white'
    ,'gold','violet','black','teal','orange']
print(len(colors))


















# Find the index
print(colors.index("gold"))

# Changing things into a list
string1 = "green"
list1 = list(string1)
print(list1)

for character in list1:
    if character == "e":
        # replace with a *
        current_index = list1.index(character)
        list1.pop(current_index)
        list1.insert(current_index, "*")

# Changing lists into strings
print("".join(list1))

