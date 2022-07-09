import datetime
import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())

if n == 0:
    print(0)
else:
    arr = [input().split() for i in range(n)]
    for i in range(n):
        arr[i][2] = int(arr[i][2])
    p = [0]*n
    t = [0]*n
    for i in range(n):
        x,y,z = arr[i][0].split('/')
        d = x+y+z
        past = datetime.datetime.strptime(arr[i][0]+" "+arr[i][1], '%Y/%m/%d %H:%M:%S')
        t[i] = past
    for i in range(n):
        t[i] = (t[-1]-t[i])
        t[i] = t[i].days*86400+t[i].seconds
        p[i] = max(0.5**((t[i])/365/86400),0.9**(n-i-1))
    s = sum(p)
    x = 0
    for i in range(n):
        x+=p[i]*arr[i][2]
    print(round(x/s))