if __name__ == '__main__':
    s = input()
    def alphanum(s):
        k1 = list(s) 
        lis1 = []
        for n1 in k1:
            if n1.isalnum() is True:
                lis1.append(True)
            else:
                lis1.append(False)
        if True in lis1:
            return True
        else:
            return False
    def alphab(s):
        k2 = list(s) 
        lis2 = []
        for n2 in k2:
            if n2.isalpha() is True:
                lis2.append(True)
            else:
                lis2.append(False)
        if True in lis2:
            return True
        else:
            return False
    def digit(s):
        k3 = list(s) 
        lis3 = []
        for n3 in k3:
            if n3.isdigit() is True:
                lis3.append(True)
            else:
                lis3.append(False)
        if True in lis3:
            return True
        else:
            return False
    def lower(s):
        k4 = list(s) 
        lis4 = []
        for n4 in k4:
            if n4.islower() is True:
                lis4.append(True)
            else:
                lis4.append(False)
        if True in lis4:
            return True
        else:
            return False
    def upper(s):
        
        k5 = list(s) 
        lis5 = []
        for n5 in k5:
            if n5.isupper() is True:
                lis5.append(True)
            else:
                lis5.append(False)
        if True in lis5:
            return True
        else:
            return False
    res1 = alphanum(s)
    print(res1)
    res2 = alphab(s)
    print(res2)
    res3 = digit(s)
    print(res3)
    res4 = lower(s)
    print(res4)
    res5 = upper(s)
    print(res5)