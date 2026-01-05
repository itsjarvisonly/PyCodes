#Question link https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true
"""Now, let's use our knowledge of sets and help Mickey.

Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

# Formula used:"""
# average = total of heights/ number of distinct heights
"""different set methods
1. add
2. update() to add to add items from an iterable
3. union,intersection,methods
4. """

#Q2
"""Given 2 sets of integers, M and N, print their symmetric difference in ascending order.
The term symmetric difference indicates those values that exist in either  M
or N but do not exist in both."""

nA = int(input().strip())
A = set(input().strip().split(" "))
nB = int(input().strip())
B = set(input().strip().split(" "))
diff1 = A.difference(B)
diff2 = B.difference(A)
final = list(diff1.union(diff2))
final = list(map(int,final))
final.sort()
for i in final:
    print(i)
    
#used strip for removing whitespaces

