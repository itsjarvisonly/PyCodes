# A very good string challenge

string = "AABCAAADA"
k = int(input("Enter the number"))
for i in range(0,len(string),k):
    sub = (string[i:i+k:])
    seen = set()
    lis = []
    for x in sub:
        if x not in seen:
            lis.append(x)
            seen.add(x)
    print("".join(lis))
    




# Remember in slicing [start:stop:step]
# def merge_the_tools(string, k):
#     f = string 

# if __name__ == '__main__':
#     string, k = input("Enter string "), int(input("Give integer"))
#     merge_the_tools(string, k)





"""Consider the following:

A string, , of length  where .
An integer, , where  is a factor of .
We can split  into  substrings where each subtring, , consists of a contiguous block of  characters in . Then, use each  to create string  such that:

The characters in  are a subsequence of the characters in .
Any repeat occurrence of a character is removed from the string such that each character in  occurs exactly once. In other words, if the character at some index  in  occurs at a previous index  in , then do not include the character in string .
Given  and , print  lines where each line  denotes string .

Example


There are three substrings of length  to consider: 'AAA', 'BCA' and 'DDE'. The first substring is all 'A' characters, so . The second substring has all distinct characters, so . The third substring has  different characters, so . Note that a subsequence maintains the original order of characters encountered. The order of characters in each subsequence shown is important.

Function Description

Complete the merge_the_tools function in the editor below.

merge_the_tools has the following parameters:

string s: the string to analyze
int k: the size of substrings to analyze
Prints

Print each subsequence on a new line. There will be  of them. No return value is expected.

Input Format

The first line contains a single string, .
The second line contains an integer, , the length of each substring.

Constraints

, where  is the length of 
It is guaranteed that  is a multiple of .
"""