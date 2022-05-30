# Question 47
#  Write a Python program to convert a given list of strings into list of lists.
# Original list of strings:
# ['Red', 'Maroon', 'Yellow', 'Olive']
# Convert the said list of strings into list of lists:

# [['R', 'e', 'd'], ['M', 'a', 'r', 'o', 'o', 'n'], ['Y', 'e', 'l', 'l', 'o', 'w'],
#  ['O', 'l', 'i', 'v', 'e']]


lists = ['Red', 'Maroon', 'Yellow', 'Olive']
s = []
for i in lists:
    a = list((i))
    s = s+[a]
print(s)
