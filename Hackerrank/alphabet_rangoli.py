def print_rangoli(size):
    # your code goes here
    max = ord("a")+ size - 1
    l,b = size*2-1,4*size - 3
    half1 = []
    rangoli_rows = []
    k = size
    for i in range(size):
        half1.append(chr(max - i))
        half2 = half1[::-1]
        half2 = half2[1:]
        full = half1 + half2
        midline = "-".join(full)
        rangoli_rows.append(midline.center(b,'-'))
        rem_rows = rangoli_rows[::-1]
        rem_rows = rem_rows[1:]
    final = rangoli_rows + rem_rows
    for n in final:
        print(n)

        # print(midline.center(b,'-'))
        
    
    
    
    
    
    
    
    
    
    # l,b = size*2-1,(size*2-1)*2-1
    # k = size
    # for i in range(size):
    #     print(str(lis[k-1]).center(b,"-"))
    #     if k > 1:
    #         k -= 1
    # for i in range(size-1):
    #     print(str(lis[k]).center(b,"-"))
    #     if k <= size:
    #         k += 1



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
# needed output
#  --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# # --------e--------

    
    
  