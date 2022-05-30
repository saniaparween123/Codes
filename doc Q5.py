# questin 5 Count unique values inside a list.
# input_list = [1, 2, 2, 5, 8, 4, 4, 8]

# Count = 5 because [1,2,5,8,4] are unique values

list = [1, 2, 2, 5, 8, 4, 4, 8]
k = []
c = 0
for i in list:
    for j in list:
        if i not in k:
            k.append(i)
            c = c+1
print(k)
print(c)
