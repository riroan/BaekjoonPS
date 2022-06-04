import math
a = input()
b = input()
la, lb = len(a), len(b)
g = math.gcd(la, lb)
l = la*lb // g
a*=l // (la)
b*=l//(lb)
if a == b:
    print(1)
else:
    print(0)