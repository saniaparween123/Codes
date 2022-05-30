#
# Question 26
# Our task is to print the element which occurs 3 consecutive
#  times in a Python list.
# Example:

# Input: [4, 5, 5, 5, 3, 8]

# Output: 5

# Input: [1, 1, 1, 64, 23, 64, 22, 22, 22]

# Output: 1, 22


list = [1, 1, 1, 64, 23, 64, 22, 22, 22]
k = []
for i in list:
    for j in list:
        c = list.count(i)
    if c >= 3:
        if i not in k:
            k.append(i)
print(k)
