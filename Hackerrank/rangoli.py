def print_rangoli(size):
    # your code goes here
    lis = list("abcdefghijklmnopqrstuvwxyz")
    for x in range(size-1):
      lmax = (size + size -1)*2 - 1 
      print("-"*lmax + )
    

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

    
    
  