# # using sort function accending and deccending


marks = [30, 50, 20, 10, 40]
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)


# # without using sortfunction
# # accending order

marks = [30, 50, 20, 10, 40]
for i in range(len(marks)):
    for j in range(len(marks)):
        if marks[i] < marks[j]:
            marks[i], marks[j] = marks[j], marks[i]
print(marks)


# # without using sort function
# # deccending order

marks = [30, 50, 20, 10, 40]
for i in range(len(marks)):
    for j in range(i+1, len(marks)):
        if marks[i] < marks[j]:
            marks[i], marks[j] = marks[j], marks[i]
print(marks)
