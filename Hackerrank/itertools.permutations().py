from itertools import permutations
in1 = "HACK 2"
in1 = in1.split(" ")
string = in1[0]
k = int(in1[1])
lis = list(string)
lis.sort()
ans = list(permutations(lis, k))
for i in ans:
    print("".join(list(i)))

#Theroy
"""This tool returns successive  length permutations of elements in an iterable.

If  is not specified or is None, then  defaults to the length of the iterable, and all possible full length permutations are generated.

Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order."""