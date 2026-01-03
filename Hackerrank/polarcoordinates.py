"""Polar coordinates are an alternative way of representing Cartesian coordinates or Complex Numbers.
"""
import cmath as cm
# z = "1+2j"
z = input()
z = complex(z) 
phase = cm.phase(z) 
r = abs(z)
print(f"{phase:.3f}\n{r:.3f}")