from itertools import product
in1 = "2 4"
in2 = "3 1"
in1 = in1.split(" ")
in1 = list(map(int,in1))
in2 = in2.split(" ")
in2 = list(map(int,in2))
# print(in1)
# print(in2)
ans = list(product(in1,in2))
ans = " ".join(str(x) for x in ans)
print(ans)

"""IT TOOK A LOT OF TIME BUT FINALLY FINISHED IT USING 1 MAP FUNCTION AND GENERATOR"""