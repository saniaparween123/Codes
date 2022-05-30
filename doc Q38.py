# Question 38

# Write a Python program to check if a given string contains an element,
# which is present in a list.
# The original string and list:

# https://www.w3resource.com/python-exercises/list/

# ['.com', '.edu', '.tv']

# Check if https://www.w3resource.com/python-exercises/list/ contains an element,
#  which is present in the list ['.com', '.edu', '.tv']

# True

# The original string and list: https://www.w3resource.net

# https://www.w3resource.net

# ['.com', '.edu', '.tv']

# Check if https://www.w3resource.net contains an element,
#  which is present in the list ['.com', '.edu', '.tv']

# False


string = "https://www.w3resource.com/python-exercises/list/"
list = ['.com', '.edu', '.tv']
length = len(list)
for x in list:
    count = 0
    if x in string:
        count = count+1
if length == count:
    print("True")
else:
    print("False")
