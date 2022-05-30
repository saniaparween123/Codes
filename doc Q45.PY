# Question 45

# Write a Python program to remove the last N number of elements from a given list.
# Original lists:
# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]

# Remove the last 3 elements from the said list:
# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34]

# Remove the last 5 elements from the said list:
# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34]

# Remove the last 1 element from the said list:
# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3]

list1 = [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
q1 = list1[:13]
q2 = list1[:11]
q3 = list1[:15]
print(q1)
print(q2)
print(q3)
