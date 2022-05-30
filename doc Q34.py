# Question 34
# Write a Python program to remove all the values except integer values from
# a given array of mixed values.
# Original list: [34.67, 12, -94.89, 'Python', 0, 'C#']

# After removing all the values except integer values from the said array
#  of mixed values: [12, 0]


list = [34.67, 12, -94.89, 'Python', 0, 'C#']
k = []
for i in list:
    if type(i) == str:
        pass
    elif type(i) == float:
        pass
    elif i >= 0:
        k.append(i)
print(k)
