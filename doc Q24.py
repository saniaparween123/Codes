# # Question 24
# Remove duplicates from a list.
# List = [1,2,3,1,2,2]

# Output: [1,2,3]

list = [1, 2, 3, 1, 2, 2]
k = []
for i in list:
    if i not in k:
        k.append(i)
print(k)



