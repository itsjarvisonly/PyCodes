x = int(input())
y = int(input())
z = int(input())
n = int(input())
lis = []
for a in range(x+1):
  i = a
  for b in range(y + 1):
    j = b
    for c in range(z+1):
      k = c
      if i+j+k != n:
        l = [i,j,k]
        lis.append(l)
print(lis)
