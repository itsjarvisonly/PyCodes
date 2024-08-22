#  Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) 
#  of any student(s) having the second lowest grade.
#  Note: If there are multiple students with the second lowest grade, order their names alphabetically 
#  and print each name on a new line.
#clear up
dic1 =  {}
tmp = []
dicr= {}
for _ in range(int(input())):
  name = input()
  score = float(input())
  dic1[name] = score
for a , b in dic1.items():
  dicr[b] = a
for s , n in sorted(dicr.items()):
  tmp.append(s)
tmp = list(set(tmp))
for x , y in dicr.items():
  if x == tmp[1]:
    print(dicr[x])