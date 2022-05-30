# Write a Python program to create a list reflecting the modified run-length encoding from
# a given list of integers or a given list of characters.

# Original list:

# [1, 1, 2, 3, 4, 4, 5, 1]

# List reflecting the modified run-length encoding from the said list:
# [[2, 1], 2, 3, [2, 4], 5, 1]
# Original String:
# aabcddddadnss
# List reflecting the modified run-length encoding from the said string:
# [[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]


list1 = [1, 1, 2, 3, 4, 4, 5, 1]
k = []
i = 0
for i in list1:
    for j in list1:
        c = list1.count(i)
        if c == 1:
            s = i
        elif c > 2:
            s = [2, i]
            if (s not in k):
                k.append(s)

        else:
            s = [c, i]
        if (s not in k):
            k.append(s)
k.append(1)
print(k)


a = "aabcddddadnss"
list2 = list((a))
k = []
for i in list2:
    for j in list2:
        c = list2.count(i)
        if c == 1:
            s = i
        else:
            s = [c, i]
        if s not in k:
            k.append(s)
print(k)
