# LCM and HCF Finder

import math
a = int(input("Enter a first number:"))
b = int(input("Enter a second number:"))
print("HCF:", math.gcd(a,b))
lcm = abs(a*b)// math.gcd(a,b)
print("lCM:", lcm)