# kaun banega karoorpati


list1 = [
    "How many continents are there?",
    "What is the capital of India?",
    "NG mei kaun se course padhaya jaata hai?"
]

list2 = [
    ["Four", "Nine", "Seven", "Eight"],
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]

s = 1
l = 1
for i in list1:
    print("Apka sawal hai:-")
    print(l, i, "\n")
    l = l+1
    print("Apka options hai\n")
    if i is list1[0]:
        for j in list2[0]:
            print(s, j)
            s = s+1
            if s == 5:
                s = 1
        user = int(input("enter your option"))
        if user == 1:
            print("Congrats! Aapka answer sahi hai\n")
        else:
            print("Sadly aapka javab ga1lat hai.\n")
            print("now you are out in game")
            break

    elif i is list1[1]:
        for p in list2[1]:
            print(s, p)
            s = s+1
            if s == 5:
                s = 1
        user1 = int(input("enter your option"))
        if user1 == 4:
            print("Congrats! Aapka answer sahi hai\n")
        else:
            print("Sadly aapka javab ga1lat hai.\n")
            print("now you are out in game")
            break

    elif i is list1[2]:
        for w in list2[2]:
            print(s, w)
            s = s+1
            if s == 5:
                s = 1
        user2 = int(input("enter your option"))
        if user2 == 1:
            print("Congrats! Aapka answer sahi hai\n")
        else:
            print("Sadly aapka javab ga1lat hai.\n")
            print("now you are out in game")
            break
