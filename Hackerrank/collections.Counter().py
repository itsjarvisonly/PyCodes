# A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary 
#values
# Question link https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=false
""" Sample input
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50       """


from collections import Counter
x = int(input())
shoe = input()
shoe = (shoe.split(" "))
shoe = list(map(int,shoe))
shoe =dict(Counter(shoe))
total_cust = int(input())
total_money = 0
for cust in range(total_cust):
    size,money = list(map(int,(input().split(" "))))
    if (shoe.get(size,0)) > 0:
        total_money += (money)
        shoe[size] -= 1
print(total_money)

"""ERROR (KEY ERROR) FIXES
1. # Change this line:
# if (shoe[size]) > 0:

# To this:
if size in shoe and shoe[size] > 0:
    total_money += money
    shoe[size] -= 1
    
2. # Change this:
# shoe = dict(Counter(shoe))

# To this:
shoe = Counter(shoe)


My solution: using the .get method on dict and setting default to 0"""
