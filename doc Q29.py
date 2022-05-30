# Question 29
# Remove empty List from List
# The original list is : [5, 6, [], 3, [], [], 9]
# List after empty list removal: [5, 6, 3, 9]


List = [5, 6, [], 3, [], [], 9]
k = []
for i in List:
    if i == []:
        pass
    else:
        k.append(i)

print(k)
