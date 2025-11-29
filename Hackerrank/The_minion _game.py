#TRY 3
string = "BANANA"
letters = list(string)
stuart = 0
kevin = 0
pos = 0

for letter in letters:
    if letter in ["A","E","I","O","U"]:
        kevin += (len(string)-pos)
        pos += 1
    else:
        stuart += (len(string)-pos)
        pos += 1
if stuart > kevin:
    print("Stuart "+str(stuart))
elif stuart == kevin:
    print("Draw")
else:
    print("Kevin "+str(kevin))
#This solution works



"""
incorrect solution try 2
from collections import Counter
string = "BANANA"
letters = list(string)
stuart = []
kevin = []
pos = 0
for letter in letters:
    if letter in ["A","E","I","O","U"]:
        kevin.append(len(string)-pos)
        pos += 1
    else:
        stuart.append(len(string)-pos)
        pos += 1
if stuart > kevin:
    print("Stuart "+str(stuart))
elif stuart == kevin:
    print("Draw")
else:
    print("Kevin "+str(kevin))
"""


"""
incorrect solution: try 1
vow_word = []
cons_word = []
pos = 0
for letter in letters:
# if letter == ("A" or "E" or "I" or "O" or "U"):  'or' is not the right choice as it stops at the first check only
    if letter in ["A","E","I","O","U"]:
        for k in range(pos,len(string)):
            vow_word.append(string[pos:k+1])
    else:
        for k in range(pos,len(string)):
            cons_word.append(string[pos:k+1])
    pos += 1
stuart = sum(Counter(cons_word).values())
kevin = sum(Counter(vow_word).values())
if stuart > kevin:
    print("Stuart "+str(stuart))
elif stuart == kevin:
    print("Draw")
else:
    print("Kevin "+str(kevin))



# def minion_game(string):
#     # your code goes here
    

# if __name__ == '__main__':
#     s = input()
#     minion_game(s)
"""