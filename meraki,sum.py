# Q: How to find all pairs in an array of integers whose sum is equal to
# the given number?
# Output:-
# [[11,19], [12,18],[13,17]]

number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
sum = []
for i in n:
    if i == 14:
        break
    for j in n:
        s = i+j
        if s == 30:
            sum = sum + [[i, j]]
print(sum)
