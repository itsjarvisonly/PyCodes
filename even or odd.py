find1 = float(input("Give the number: "))
find2 = float(input("GIve divider: "))
check2 = find1 %  2
if check2 == 0:
    print("Even")
else:
    print("Odd")
check4 = find1 % 4
if check4 == 0:
    print("it is also a multiple of 4")
divisiblity = find1 % find2
if divisiblity == 0:
    print(find1 ," is divisible by " , find2)
else:
    print(find1 ," is not divisible by " , find2)
