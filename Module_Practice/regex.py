#takes a text file as input and finds all the numbers it that file and adds them up-------------
#Uses Regular Expressions for finding
import re
file = open("regexsum.txt")
lis = []
x = 0
for line in file:
    nums = re.findall('([0-9]+)',line)
    for k in nums:
        x += int(k)
print(x)