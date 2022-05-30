# Question 36

# Write a Python program to join adjacent members of a given list.
# Original list:
# ['1', '2', '3', '4', '5', '6', '7', '8']

# Join adjacent members of a given list:
# ['12', '34', '56', '78']

# Original list:

# ['1', '2', '3']
# Join adjacent members of a given list:
# ['12']


list1 = ['1', '2', '3', '4', '5', '6', '7', '8']
q1 = list1[0]+list1[1]
q2 = list1[2]+list1[3]
q3 = list1[4]+list1[5]
q4 = list1[6]+list1[7]

print([q1, q2, q3, q4])
