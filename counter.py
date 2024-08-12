# Write your code here
string = input()
strng = string.lower()
ls = []
fin = {}
for i in strng:
    ls.append(i)
for x in ls:
    if x not in fin:
        fin[x] = 1
    else: 
        fin[x] += 1
print(fin)