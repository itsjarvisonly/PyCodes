def print_formatted(num):
    width = len(f"{num:b}")
    for k in range(1, num + 1):
        dec = f"{k}"
        octal = f"{k:o}"
        hexa = f"{k:x}".upper()
        binary = f"{k:b}"
        print(f"{dec:>{width}} {octal:>{width}} {hexa:>{width}} {binary:>{width}}")
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# needed output
#     1     1     1     1
#     2     2     2    10
#     3     3     3    11
#     4     4     4   100
#     5     5     5   101
#     6     6     6   110
#     7     7     7   111
#     8    10     8  1000
#     9    11     9  1001
#    10    12     A  1010
#    11    13     B  1011
#    12    14     C  1100
#    13    15     D  1101
#    14    16     E  1110
#    15    17     F  1111
#    16    20    10 10000
#    17    21    11 10001