# Question 30
# Given a list of numbers, write a Python program to count positive
# and negative numbers in a List.

# Example:
# list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3
# Iist2 = [-12, 14, 95, 3]
# Output: pos = 3, neg = 1

list1 = [2, -7, 5, -64, -14]
p = 0
n = 0
for i in list1:
    if i > 0:
        c = list1.count(i)
        p = p+c
    else:
        s = list1.count(i)
        n = n+s
print("list1 positive num =", p, "nagative num =", n)


list2 = [-12, 14, 95, 3]
p = 0
n = 0
for i in list2:
    if i > 0:
        c = list2.count(i)
        p = p+c
    else:
        s = list2.count(i)
        n = n+s
print("list2 positive num =", p, "nagative num =", n)
