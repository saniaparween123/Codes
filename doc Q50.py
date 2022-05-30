# Write a Python program to join two given list of lists of same length, element wise.
# Original lists:
# [[10, 20], [30, 40], [50, 60], [30, 20, 80]]
# [[61], [12, 14, 15], [12, 13, 19, 20], [12]]

# Join the said two lists element wise:
# [[10, 20, 61], [30, 40, 12, 14, 15], [50, 60, 12, 13, 19, 20], [30, 20, 80, 12]]


list1 = [[10, 20], [30, 40], [50, 60], [30, 20, 80]]
list2 = [[61], [12, 14, 15], [12, 13, 19, 20], [12]]
j = 0
k = []
for i in list1:
    s = i+list2[j]
    j = j+1
    k = k+[s]
print(k)
