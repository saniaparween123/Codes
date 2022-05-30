# question 9 Find the First Maximum, Second maximum, Third maximum number from the List.

list = [4, 93, 26, 13, 10]
max1 = max(list)
print(max1)

list.remove(max1)
max2 = max(list)
print(max2)

list.remove(max2)
max3 = max(list)
print(max3)
