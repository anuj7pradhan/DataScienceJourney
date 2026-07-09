list = [1,2,3,4,5,6,7]
print(f"This is a list :{list}")

list1 = ["anuj",1,2,4,True,False,"Hello"]
print(f"This is list1:{list1}")

# Access lists items
# Positive indexing
print(f"This is positive indexing of list1: {list1[0]}")

# negative indexing
print(f"This is negative indexing of list1: {list1[-3]}")

#exclude
print(f"This is slicing of list1: {list1[2:5]}")

# slice in list
print(f"This is negative slicing of list1: {list1[-5:-1]}")

print(f"This is list1 slicing from 1:4 {list1[1:4]}")
print(f"This is list1 negative slicing from -6:-3 {list1[-6:-3]}")

print(f" This is negative list1 from -3 to end: {list1[-3:]}")
print(f" This is list1 from 0 to -3:{list1[:-3]}")

fruit_list = ["apple", "banana", "mango"]
fruit_list[2] = "papaya"
print(fruit_list)

# change range of the item values

fruit_list[:] = ["guava","watermelon","orange","pineapple","jackfruit"]
print(fruit_list)

#replacing multiple item by one item
fruit_list[1:3] = ["cherry"]
print(fruit_list)

# Adding item to the list by insert(),  extend(), and append() methods
# insert() to add item by indexing
fruit_list.insert(1,"apple")
print(fruit_list)

# append() is used to add item in a list at the last
fruit_list.append('hi')
print(fruit_list)

fruit_list.insert(3,"watermelon")
print(fruit_list)

fruit_list.append("aisel")
print(fruit_list)

fruit_list1 = ["peanuts","fruits"]
fruit_list.extend(fruit_list1)
print(fruit_list)

fruit_tuple = ("fruits", "veg")
fruit_list.extend(fruit_tuple)
print(fruit_list)

# Remove item : remove(), pop(),del, clear()
game = ["football", "basketball", "volleyball"]
game.remove("basketball")
print(game)

# pop
game1 = ["football", "basketball", "volleyball", "cricket"]
game1.pop(2)
print(game1)

# del
game2 = ["football", "basketball", "volleyball", "cricket"]
# del game2
print(game2)

game2.clear()
print(game2)


list_of_item = ["sur", "bir", 'chakra',"vir"]
list_of_item.append("bashu")
print(list_of_item)

list_of_item.pop(2)
print(list_of_item)

#del list_of_item
print(list_of_item)


list_of_item1 = ["abc", "bcd", "cde"]
list_of_item.extend(list_of_item1)
print(list_of_item)

#sorting

thislist = ["Sur", "bir", 'Chakra',"vir"]
thislist.sort()
print(thislist)

thislist.sort(reverse=True)
print(thislist)


# changing into lowercase for temporary time
thislist = ["Sur", "bir", 'Chakra',"vir"]
thislist.sort(key=str.lower)
print(thislist)

# Join

list1  = [1,2,3,45,5,6,62]
list2 = ["a","b","c"]
list3 = list1 + list2
print(list3)
print(f"{list1 + list2}")



copy_list = list1.copy()
print(copy_list)


# del
game2 = ["football", "basketball", "volleyball", "cricket"]
# del game2
print(game2)

game2.clear()
print(f"This is a clear list: {game2}")