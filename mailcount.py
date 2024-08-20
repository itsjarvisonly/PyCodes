name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
dic = {}
lis = []
for line in handle:
    if line.startswith("From "):
        part = line.split()
        name = part[1]
        lis.append(name)
for k in lis:
    dic[k] = dic.get(k , 0) + 1
large = None
largename = None
for key,values in dic.items():
    if large is None or int(values) >= int(large):
        largename = key
        large = values
print(largename , large)