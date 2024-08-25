"""Q. Write a program to print the fibonacci sequence"""
def fib(n):   
  if n == 0 :
    return 0
  elif n == 1:
    return 1
  else:
    return (fib(n-1) + fib(n-2))
for k in range(int(input("Give the number of terms you want to print:  "))): print(fib(k))
