import sys
from math import *
def input(): return sys.stdin.readline().strip()


n = int(input())
arr = []
for i in range(n+1):
    print(f"? {i+1}")
    sys.stdout.flush()
    x = int(input())
    arr.append(x)
brr = []
for i in range(1, n+2):
    tmp = []
    for j in range(n+1):
        tmp.append(i**j)
    tmp.reverse()
    tmp.append(arr[i-1])
    brr.append(tmp)
for i in range(n+1):
    for j in range(i+1, n+1):
        for k in range(n, -1, -1):
            if brr[i][k] == 0:
                continue
            if brr[j][k] % brr[i][k] == 0:
                t = brr[j][k] // brr[i][k]
                for l in range(n+2):
                    brr[j][l] -= t * brr[i][l]
                break
        g = 0
        for k in range(n+2):
            if brr[j][k] == 0:
                continue
            if g == 0:
                g = brr[j][k]
            else:
                g = gcd(g, brr[j][k])
        if g > 0:
            for k in range(n+2):
                brr[j][k] //= g

for i in range(n, -1, -1):
    for j in range(i-1, -1, -1):
        for k in range(n, -1, -1):
            if brr[i][k] == 0:
                continue
            if brr[j][k] % brr[i][k] == 0:
                t = brr[j][k] // brr[i][k]
                for l in range(n+2):
                    brr[j][l] -= t * brr[i][l]
                break
        g = 0
        for k in range(n+2):
            if brr[j][k] == 0:
                continue
            if g == 0:
                g = brr[j][k]
            else:
                g = gcd(g, brr[j][k])
        if g > 0:
            for k in range(n+2):
                brr[j][k] //= g
ans = []
for i in brr:
    ans.append(i[-1])
print('!', *ans)
sys.stdout.flush()
