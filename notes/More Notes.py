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




