list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = int(input("enter:- "))
s = []
for i in list:
    for j in list:
        c = list.count(i)
    if c >= k:
        if i not in s:
            s.append(i)
print(s)
