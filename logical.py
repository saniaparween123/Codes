a = 1245697124
l = 0
while a > 0:
    c = a % 10
    a //= 10
    if l < c:
        l = c
print(l)


a = 1245697124
b = str(a)
print(max(b))
