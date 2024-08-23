#The quick brown fox jumps over the lazy dog.
strs = input()  # Take input from the user
spt = strs.split()  # Split the input string into a list of words
lis = []
for n in spt:
    for x in range(2, len(n)):
        if len(n) % x == 0:
            lis.append(n)
for k in lis:
    if k in spt:
        spt.remove(k) 
fin = " ".join(spt)
print(fin)  # Print the final string

"""THis code prints only the odd length having words from a given string"""