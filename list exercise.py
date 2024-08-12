a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
given = input("Give the number:")
for x in a:
    if x < int(given):
        b.append(x)
print(b)