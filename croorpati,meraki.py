
# Write a program that tells in the above list that how many
# people are there in the above list who are :

# 1 - `Crorepati`
# 2 - `Lakhpati`
# 3 - `Dilwale`

# All those who have money more than or equal to 1 crore are known
#  as Crorepati. All those who have money money greater than or equal
#  to 1 lakh, those are called Lakhpati. Rest of the people are called Dilwale.
# kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000,
# 690909090, 31010101, 532010, 510, 4100]


money = [3000, 600000, 324990909, 90990900, 30000, 5600000,
         690909090, 31010101, 532010, 510, 4100]
for i in money:
    if i >= 0 and i < 100000:
        print(i, "dilwale")
    elif i >= 100000 and i < 10000000:
        print(i, "lakhpati")
    elif i >= 10000000:
        print(i, "crorpati")
