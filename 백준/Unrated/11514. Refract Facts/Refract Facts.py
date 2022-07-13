import sys
from math import *
input = lambda: sys.stdin.readline().strip()

while True:
    d,h,x,n1,n2=map(float, input().split())
    if d==h==x==n1==n2==0:
        break
    l=0
    r = pi/2
    while r-l>1e-6:
        mid = (l+r)/2
        t1 = pi/2 - mid
        t2 = asin(n2/n1*sin(t1))
        if d*tan(t1)+ h*tan(t2) > x:
            l = mid
        else:
            r = mid
    print("{:.2f}".format(round(mid*180/pi,2)))