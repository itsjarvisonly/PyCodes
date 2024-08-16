n = int(input())
arr = map(int, input().split())
lis = list(arr)
begin = None
s = 0
for i in lis:
  if begin is None:
    begin = i
  if i >= begin:
    begin = i
for k in range(i):
  if k in lis:
    runnerup = k
print(runnerup)