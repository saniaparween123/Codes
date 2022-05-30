# Write a Python program to find the list with maximum and minimum length.
# Original list:

# [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:

# (1, [0])


list = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
maximum = max(list)
minimum = min(list)

print([len(maximum), maximum])
print([len(minimum), minimum])
