from math import log2
n,p = map(int, input().split())
if n == 1:
    print("0.000000")
else:
    print("{:.6f}".format(round((1-n)*(log2(p)-log2(360))-log2(n),6)))