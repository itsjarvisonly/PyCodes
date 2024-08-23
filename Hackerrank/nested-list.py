"""
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) 
of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically 
and print each name on a new line.
"""
dic = {}                                       #used data sets
lis1 = []                                      #used data sets
scores = []                                    #used data sets
names = []                                     #used data sets
n = None
for _ in range(int(input())):                  #takes input and store them in nested lists
    name = input()
    score = float(input())
    lis1.append([name, score])
for row in lis1:
    scores.append(row[1])
lisn = sorted(list(set(scores)), reverse=True) #I sorted the list lisn because i was getting an error due to unordered data
for k in lisn:                                 #finds the second lowest grade
    if n is None:
        n = k
    if k > min(lisn) and k <= n:
        n = k
for row in lis1:                               #order the names alphabetically
    if row[1] == n:
        names.append(row[0])
fin = names.sort()
for o in names:
    print(o)

"""Example input
        5
        Harry
        37.21
        Berry
        37.21
        Tina
        37.2
        Akriti
        41
        Harsh
        39
"""