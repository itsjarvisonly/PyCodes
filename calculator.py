"""This is a calculator that can do mathematical operations on N numbers as input provided"""
def calc(ans,opp,num2):
  if opp == "+":
    return float(ans) + float(num2)
  if opp == "-":
    return float(ans) - float(num2)
  if opp == "*":
    return float(ans) * float(num2)
  if opp == "/":
    return float(ans) / float(num2)
  else: print(" Please give operator as + or - or * or /")
n = int(input("How many numbers you want to do work on at a time: "))
ans = input("Give number 1: ")
data = [ans]
for _ in range(n-1):
  opp = input("what to do ( + / - / * or /) : ")
  num2 = input("Give next number: ")
  ans = calc(ans,opp,num2)
  data.append((opp,num2))
  print("This step answer is: ",ans)
print("Your final answer is: ",ans)
lis = input("Do you want to see list of all the numbers you used y/n:  ")
if lis == "y" or lis == "Y":
  print(data)
else: print("Done!")