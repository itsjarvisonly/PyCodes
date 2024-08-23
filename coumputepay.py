"""This code is a solution of py4e autograder of calculating the pay for workers in a company"""
#If you want to know more do refer tohttps://www.py4e.com/tools/pythonauto/?PHPSESSID=6992ac77beceb854a79cf44906aa6871
def computepay(h, r):
    if h >= 40:
        pay = (40*r + ( h % 40)* r * 1.5)
    return pay
hrs = float(input("Enter Hours:"))
rate = float((input('Enter Rate')))
p = computepay(hrs, rate)
print("Pay", p)
