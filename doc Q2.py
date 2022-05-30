# Convert Character Matrix to single String;
# he original list is: [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]

# The String after join: gfgisbest


list = [['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]
s = ""
for i in list:
    for j in i:
        s = s+j
print(s)
