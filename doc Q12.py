# Question 12.
# You will be given a number and you need to return it as a string in
# Expanded Form. For example:

# 12  # Should return '10 + 2'

# 42 # Should return '40 + 2'

# 70304  # Should return '70000 + 300 + 4'


num = 70304
k = 4
c = str(num)
a = list((c))
for i in a:
    if i == "0":
        s = "+"
        print(s, end="")
    else:
        s = k*'0'
        print(i+s, end="")
        k = k-2
