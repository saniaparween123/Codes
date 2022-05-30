# magic squade


lists = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
t = 0
w = 0
v = 0
for i in lists:

    if i == lists[0]:
        a = sum(lists[0])
    elif i == lists[1]:
        b = sum(lists[1])
    elif i == lists[2]:
        c = sum(lists[2])

        for j in lists:
            t = t+j[0]
            w = w+j[1]
            v = v+j[2]

if a == b == c == t == w == v:
    print("magic squade")
else:
    print("not a magic squade")


# magic squade


lists = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
i = 0
a, b, c, d, e, f, g, h = 0, 0, 0, 0, 0, 0, 0, 0
while i < len(lists):

    a = a+lists[i][0]
    b = b+lists[i][1]
    c = c+lists[i][2]
    d = d+lists[0][i]
    e = e+lists[1][i]
    f = f+lists[2][i]
    g = g+lists[i][i]
    h = h+lists[i][2-i]

    i = i+1
if a == b == c == d == e == f == g == h:
    print("magic squade")
else:
    print("not magic squade")
