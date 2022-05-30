# These are the marks of any student for the last three years.
#  You have to calculate total marks for all the three years.

# Sum of the nested list given above - 1142.


marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
]

print(sum(marks[0]+marks[1]+marks[2]))


# Sum of the nested list given above - 965.
marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78]
]

print(sum(marks[0]+marks[1]+marks[2]))


# Sum of the nested list given above - 1324.

marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78],
    [87, 67, 49, 68, 88]
]

print(sum(marks[0]+marks[1]+marks[2]+marks[3]))


# This is the list of marks of a student for the last three years. You have to calculate the average marks for each year.
# Like, for the above list, the output should be as follows:-
# Average of 1 year - 84
# Average of 2 year - 80
# Average of 3 year - 63

marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
]

year1 = sum(marks[0])//5
year2 = sum(marks[1])//5
year3 = sum(marks[2])//5

print("Average of 1 year", year1)
print("Average of 2 year", year2)
print("Average of 3 year", year3)
