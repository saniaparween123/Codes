# Question 40

# Write a Python program to sum two or more lists, the lengths of
# the lists may be different.
# Original list:

# [[1, 2, 4], [2, 4, 4], [1, 2]]

# Sum said lists with different lengths:

# [4, 8, 8]

# Original list:


list1 = [[1, 2, 4], [2, 4, 4], [1, 2]]
l, l1, l2 = 0, 0, 0
for x in list1:
    i = 0
    while i < len(x):
        if i == 0:
            l = l+x[i]
        elif i == 1:
            l1 = l1+x[i]
        elif i == 2:
            l2 = l2+x[i]
        i = i+1
print([l, l1, l2])
