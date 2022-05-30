# Write a code that works for any list, it should give two
#  sums as outputs, one is the sum of odd numbers present in
# the list and the other is the sum of even numbers present in the list.

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
c_e = 0
c_o = 0
for i in elements:
    if i % 2 == 0:
        c_e = c_e+i
    else:
        c_o = c_o+i
print("even numbers:-", c_e)
print("odd numbers:-", c_o)
