# Question 39

# Write a Python program to compute the average of nth elements in a given
# list of lists with different lengths.
# Original list:

# [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]

# Average of n-th elements in the said list of lists with different lengths:

# [4.8, 5.8, 6.8, 8.0, 11.0]


list1 = [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
l, l1, l2, l3, l4 = 0, 0, 0, 0, 0
c, c1, c2, c3, c4 = 0, 0, 0, 0, 0
for x in list1:
    i = 0
    while i < len(x):
        if i == 0:
            l = l+x[i]
            c = c+1
        elif i == 1:
            l1 = l1+x[i]
            c1 = c1+1
        elif i == 2:
            l2 = l2+x[i]
            c2 = c2+1
        elif i == 3:
            l3 = l3+x[i]
            c3 = c3+1
        elif i == 4:
            l4 = l4+x[i]
            c4 = c4+1
        i = i+1

print([l/c, l1/c1, l2/c2, l3/c3, l4/c4])
