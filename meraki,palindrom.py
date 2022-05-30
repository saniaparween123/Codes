# Write a code that checks whether a list is a palindrome or not.
# And print “Haan! palindrome hai” if its a pallindrome and
# “nahi! palindrome nahi hai” if its not a palindrome.


name = ['n', 'i', 't', 'i', 'n']
reverse = name[::-1]
if name == reverse:
    print("Haan! palindrome hai")
else:
    print("nahi! palindrome nahi hai")
