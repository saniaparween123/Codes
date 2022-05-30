# Question 35
# Write a Python program to check if first digit/character of
#  each element in a given list is same or not.
# Original list:
# [1234, 122, 1984, 19372, 100]

# Check if first digit in each element of the said given list
#  is same or not!
# True
# Original list:
# [1234, 922, 1984, 19372, 100]


list = [1234, 122, 1984, 19372, 100]
l = len(list)
c = 0
for i in list:
    r = str(i)
    if r[0] == "1":
        c = c+1
if l == c:
    print('True')
else:
    print("False")
