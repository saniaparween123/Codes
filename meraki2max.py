# Write a Code that finds second maximum element from the list and print it.

numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
max1 = max(numbers)
numbers.remove(max1)
max2 = max(numbers)
print(max2)
