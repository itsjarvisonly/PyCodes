import math as m
# ABC is a right triangle, 90degree at B.
# Therefore, angle ABC = 90 degree .

# Point M is the midpoint of hypotenuse AC.

# You are given the lengths AB and BC.
# Your task is to find angle MBC in degrees.
# (link to image https://s3.amazonaws.com/hr-challenge-images/9668/1440151155-10b2b748ee-rsz_1438840048-2cf71ed69d-findangle.png)
# link to question (https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true)

"""Input Format

The first line contains the length of side AB.
The second line contains the length of side BC.
Output angle MBC in degrees."""

AB = float(input())
BC = float(input())
HYP = m.sqrt((AB**2)+(BC**2))
MC = HYP/2
angleMCB = m.acos(BC/HYP)
MB = m.sqrt((BC**2) + (MC**2) - 2*BC*MC*m.cos(angleMCB))
theta = m.asin((MC*m.sin(angleMCB))/MB)
print(str(round(m.degrees(theta)))+chr(0xb0))

# this is my solution as i didnt remember that the midpoint of hypotenuse is equidistanct from all vertices
#otherwise the answer would be just tan inverse of AB/BC

"""What new i learned:
1. Using some functions of math module
2. Using the angles in radians and degrees
3. How to add character like degree symbols in python
4. revise sine and cosine formula 
5. integrating geometry with python solving
"""