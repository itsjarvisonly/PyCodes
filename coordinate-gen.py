"""This program makes all the comination of co-ordinates up to x,y,z from 0,0,0  
given x,y and z """
x = int(input())
y = int(input())
z = int(input())
n = int(input())
for a in range(x + 1):
    for b in range(y + 1):
        for c in range(z + 1):
            print([a, b, c])