#!/bin/python3

import math
import os
import random
import re
import sys
if __name__ == '__main__':
    t = int(input().strip())
    lis = []
    add = 0
    ans = []
    for t_itr in range(t):
        n = int(input().strip())
        for x in range(1,n):
          if x % 3 == 0 or x % 5 == 0:
            lis.append(x)
        for k in lis:
          add += k
        ans.append(add)
        lis = []
        add = 0
    for l in ans:
      print(l)
