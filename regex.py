import re
file = open("test.txt")
for line in file:
    lis = re.findall('[0-9]+',line)
print(lis)




