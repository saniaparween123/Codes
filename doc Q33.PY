# Question 33
# Find the sum of number digits in List.
# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]
# Explanation: 1+2 = 3, 6+7=13, 9+8=17, 3+4=7


list1 = [15, 81, 11, 234]
for i in list1:
    a = i % 10
    b = i//10
    print(a+b, end=",")
