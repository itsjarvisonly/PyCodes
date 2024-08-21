#  Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) 
#  of any student(s) having the second lowest grade.
#  Note: If there are multiple students with the second lowest grade, order their names alphabetically 
#  and print each name on a new line.

dic1 = {}
dicr = {}
tmp = []
lis = []
k = None
for _ in range(int(input())):
    name = input()
    score = float(input())
    dic1[name] = score
for n,s in dic1.items():
    tmp.append((s,n))
for s,t in sorted(tmp, reverse=True):
    if k is None:
        k = float(s)
    if s not in lis:
        lis.append(s)
for  