# Duplicates

# Take out the duplicates from this list and put it in different list and
#  print it.

n = [19, 17, 12, 17, 17, 18, 10, 17, 14]

k = []
for i in n:
    for j in n:
        c = n.count(i)
    if c >= 2:
        k.append(i)
print(k)


# Duplicates

# Take out the duplicates from this list and put it in different list and
#  print it.


n = [19, 17, 12, 17, 17, 18, 10, 17, 14]
r = []
k = []
for i in n:
    for j in n:
        c = n.count(i)
        s = i
        if (s not in k):
            k.append(s)
    if c >= 2:
        r.append(i)
print(r)
print(k)
