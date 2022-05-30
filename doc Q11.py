
#  question 11. For example, if we give 9119  the function should return  811181, as the  square of
#  9 is 81 and square of 1  is 1.


num = 9119
a = str(num)
i = 0
s = ""
while i < len(a):
    s = (int(a[i])**2)
    i = i+1
    print(s, end="")
