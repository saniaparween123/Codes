# Write a code that works for any list, and that tells how many
#  odd numbers and how many even numbers are there in a given list.

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
c_e = 0
c_o = 0
for i in elements:
    if i % 2 == 0:
        c_e = c_e+1
    else:
        c_o = c_o+1
print("even numbers:-", c_e)
print("odd numbers:-", c_o)
