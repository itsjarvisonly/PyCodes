given = int(input("Give the number: "))
lis = range(1 ,given)
final = []
for i in lis:
    print(i)
    if given % i == 0:
        final.append(i)
print(final)