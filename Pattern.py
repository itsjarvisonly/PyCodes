x = map(int, input().split())       # Read and convert input values for x and 
y = map(int, input().split())
x = list(x)
y = list(y)
for i in x:                         # Print pairs [i, j] for each element in x and y
  for j in y:
    print([i , j])