
# Write a function that takes one argument “n” and delete that
#  many elements from the list.

# delete_nth ([1,1,1,1],2) # return [1,1]

# delete_nth ([20,37,20,21],1) # return [20,37,21]


list1 = [1, 1, 1, 1]
list2 = [20, 37, 20, 21]

del list1[0:2]
del list2[2]

print(list1)
print(list2)
