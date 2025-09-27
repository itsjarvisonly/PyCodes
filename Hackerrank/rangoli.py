def print_rangoli(size):
    # your code goes here
    lis = list("abcdefghijklmnopqrstuvwxyz")
    k = size
    for x in range(k):
      l = (k*2-1)*2 - 1 
      print(int((l-1)/2)*"-", end= "")
      print(lis[k-1], end="")
      print(int((l-1)/2)*"-")
      k -= 1
    






if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
# # needed output
##  --------e--------
# # ------e-d-e------
# # ----e-d-c-d-e----
# # --e-d-c-b-c-d-e--
# # e-d-c-b-a-b-c-d-e
# # --e-d-c-b-c-d-e--
# # ----e-d-c-d-e----
# # ------e-d-e------
# # --------e--------

    
    
  