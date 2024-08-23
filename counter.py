# Prompt the user to input a string and convert it to lowercase
string = input()
strng = string.lower()
# Initialize an empty list and dictionary
ls = []
fin = {}
# Append each character of the string to the list
for i in strng:
    ls.append(i)
# Count the occurrences of each character
for x in ls:
    if x not in fin:
        fin[x] = 1
    else: 
        fin[x] += 1
# Print the dictionary with character counts
print(fin)


"""These comments are generated later with AI just to explain the code, code is my own"""