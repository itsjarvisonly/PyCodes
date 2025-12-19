from itertools import combinations
in1 = "HACK 2"
in1 = in1.split(" ")
k = int(in1[1])
string = in1[0]
lis = list(string)
lis.sort()
for s in range(1,k+1):
    ans = list(combinations(lis,s))
    # print(ans)
    for i in ans:
        print("".join(i))