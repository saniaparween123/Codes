#  QUESTION 4
# List product excluding duplicates.
# List = [6,1,3,5,6,3,1]
# Output: 90


n = [6, 1, 3, 5, 6, 3, 1]
s = 1
for i in n:
    for j in n:
        c = n.count(i)
        if c >= 2:
            n.remove(i)

for j in n:
    s = s*j
print(s)


n = [6, 1, 3, 5, 6, 3, 1]
k = []
s = 1
for i in n:
    if i not in k:
        k.append(i)
for j in k:
    s = s*j
print(s)
