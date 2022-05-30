# Write a code, that counts the numbers between 20 and 40 and
# then print its count
# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
count = 0
for i in numbers:
    if i >= 20 and i <= 40:
        count = count+1
print(count)
