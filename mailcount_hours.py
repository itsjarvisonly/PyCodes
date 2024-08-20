name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name, "r")
lst1 = []
lst2 = []
dic1 = {}
for line in handle:
    if line.startswith("From "):
        words = line.split()
        lst1.append(words[5])
for time in lst1:
    hour = time.split(":")
    lst2.append(hour[0])
for h in lst2:
    dic1[h] = dic1.get(h ,0) +1
fin = sorted(dic1.items())
for k,v in fin:
    print(k,v)