# Write a code that works for any list, it shows the two averages
# as the output. One is the average of even numbers and the other is
# the average of odd numbers from the given list.

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
s_odd = 0
s_even = 0
c_even = 0
c_odd = 0
for i in elements:
    if i % 2 == 0:
        c_even = c_even+i
        s_even = s_even+1
    else:
        c_odd = c_odd+i
        s_odd = s_odd+1
ave_even = c_even/s_even
ave_odd = c_odd/s_odd
print("average of even numbers:-", ave_even)
print("average of odd numbers:-", ave_odd)


# count of odd numbers ….
# count of even numbers ….
# count of all the numbers ….
# sum of odd numbers ….
# sum of even numbers ….
# sum of all the numbers ….
# average of odd numbers ….
# average of even numbers ….
# average of all the numbers ka ….


elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
s_odd = 0
s_even = 0
c_even = 0
c_odd = 0
for i in elements:
    if i % 2 == 0:
        s_even = s_even+i
        c_even = c_even+1
    else:
        s_odd = s_odd+i
        c_odd = c_odd+1
ave_even = s_even/c_even
ave_odd = s_odd/c_odd
sum = s_odd+s_even
length = len(elements)

print("count of even numbers", c_even)
print("count of odd numbers", c_odd)
print("count of all number", length)

print("\nsum of all even numbers", s_even)
print("sum of all odd numbers", s_odd)
print("sum of all list numbers", sum)

print("\naverage of even numbers:-", ave_even)
print("average of odd numbers:-", ave_odd)
print("average of all list numbers", sum/length)
