# Question  42
#
#  Write a Python program to iterate a given list cyclically on specific index position.
# Original list:

# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# Iterate the said list cyclically on specific index position 3 :

# ['d', 'e', 'f', 'g', 'h', 'a', 'b', 'c']

# Iterate the said list cyclically on specific index position 5 :

# ['f', 'g', 'h', 'a', 'b', 'c', 'd', 'e']


list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
q1 = list1[3:]+list1[:3]
print(q1)
q2 = list1[5:]+list1[:5]
print(q2)
