# Q: Given two arrays, 1,2,3,4,5,6 and [2,3,1,0,6,7] find which numbers
# are not present in the second array.
# Output:-
# [4, 5]

list1 = [1, 2, 3, 4, 5, 6]
list2 = [2, 3, 1, 0, 6, 7]
num = []
for i in list1:
    if i not in list2:
        num = num+[i]
print(num)
