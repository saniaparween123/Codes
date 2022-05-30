# convert to binary number in decimal form.


binary_number = [1, 0, 0, 1, 1, 0, 1, 1]
reverse = binary_number[::-1]
r = 0
t = 0
for i in reverse:
    p = i*(2**t)
    t = t+1
    r = r+p
print(r)
