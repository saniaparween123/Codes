# Question 31

# Given the start and end of a range, write a Python program to print
# all negative numbers in a given range.
# Example:
# Input: start = -4, end = 5
# Output: -4, -3, -2, -1
# Input: start = -3, end = 4
# Output: -3, -2, -1

s = 1
start = int(input("enter starting :- "))
end = int(input("enter ending :- "))
for i in range(-start, -end):
    s = i+1
    print(s, end=",")


# que_list = ["Who Invented computer", "Who invented Internet",
#             "When was python developed", "what is the fullform of www."]
# opt_list = [["Vint cerf", "Mark Jukerberg", "Charls babbage", "Robert Vintage"], ["Vint cerf", "vinton cerf", "Guido", "John babbage"], [
#     "21 feb", "20 feb", "20 march", "19 jan"], ["world web wide", "world wide web", "world web webside", "world wide webside"]]
# ans_list = [3, 1, 2, 2]
# fifty_list = [["Charls babbage", "Robert Vintage"], ["vint cef", "guido"], [
#     "21 feb", "20 feb"], ["world web wide", "world wide web"]]
# sol_list = [1, 1, 2, 2]
# lifelinecount = 0


# def lifeline(index):
#     global lifelinecount
#     j = 0
#     if(lifelinecount == 0):
#         while j < len(fifty_list[index]):
#             print(j+1, fifty_list[index][j])
#             j = j+1
#         user_ans = int(input('.....'))
#         lifelinecount += 1
#         if user_ans == sol_list[index]:
#             return True
#         else:
#             return False
#     else:
#         print('you Already used 5050')
#         return "no"


# def option(index):
#     j = 0
#     while j < len(opt_list[index]):
#         print(j+1, opt_list[index][j])
#         j = j+1
#     user_ans = int(input('.....'))
#     if user_ans == ans_list[index]:
#         return True
#     if user_ans == 5050:
#         return(lifeline(index))
#     else:
#         return False


# def que():
#     index = 0
#     while index < len(que_list):
#         print("Q.", index+1, que_list[index], "?")
#         result = option(index)
#         if result == "no":
#             index -= 1
#         elif result == True:
#             print("Congractualtion")
#         else:
#             print("you Losse !")
#             break
#         index += 1


# def main():
#     que()


# main()
