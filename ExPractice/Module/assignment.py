# Find the intersection (Common elements) of Two Lists?

list1 = [1,2,4,5]
list2 = [4,5,6,7,8]

# Using for loop
def intersection_loop(lst1,lst2):
    common_list = []
    for item in lst1:
        if item in lst2 and item not in common_list:
            common_list.append(item)
    return common_list
print(intersection_loop(list1, list2))
# Using list comprehensive