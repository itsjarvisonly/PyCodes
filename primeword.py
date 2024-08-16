#The quick brown fox jumps over the lazy dog.
strs = input()
spt = strs.split()
lis = []
for n in spt:
  for x in range(2, len(n)):
    if len(n) % x == 0:
      lis.append(n)
for k in lis:
  if k in spt:
    spt.remove(k)
fin = " ".join(spt)
print(fin)