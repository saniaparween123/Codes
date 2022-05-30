# Question 41
# Write a Python program to find the dimension of a given matrix.
# Original list:
# [[1, 2], [2, 4]]
# Dimension of the said matrix:
# (2, 2)
# Original list:
# [[0, 1, 2], [2, 4, 5]]
# Dimension of the said matrix:
# (2, 3)
# Original list:
# [[0, 1, 2], [2, 4, 5], [2, 3, 4]]
# Dimension of the said matrix:
# (3, 3)


list1 = [[0, 1, 2], [2, 4, 5]]
row = 0
colun = 0
for i in list1:
    row = row + 1
for j in i:
    colun = colun+1
print(row, colun)
