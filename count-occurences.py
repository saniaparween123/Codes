#  is made from the word occur which means that how many times
#  a certain character or word appears.
# char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u",
# "g", "a", "x", "a"]

# Output of the Sample List
# [["a", 6], ["n", 3], ["t", 2], ["x", 2], ["u", 1], ["g", 1]]

# a - 6 times
# n - 3 times
# t - 2 times
# x - 2 times
# u - 1 times
# g - 1 times


char_list = ["a", "n", "t", "a", "a", "t", "n",
             "n", "a", "x", "u", "g", "a", "x", "a"]
k = []
for i in char_list:
    for j in char_list:
        c = char_list.count(i)
        s = [i, c]
        if (s not in k):
            k.append(s)
print(k, end=" ")
