def print_rangoli(size):
    # your code goes here
    lis = list("abcdefghijklmnopqrstuvwxyz")
    l,b = size*2-1,(size*2-1)*2-1
    k = size
    for i in range(size):
        print(str(lis[k-1]).center(b,"-"))
        if k > 1:
            k -= 1
    for i in range(size-1):
        print(str(lis[k]).center(b,"-"))
        if k <= size:
            k += 1
        
        
        
    
    






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

    
    
  