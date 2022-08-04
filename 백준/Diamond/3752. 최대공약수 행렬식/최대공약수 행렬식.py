from collections import defaultdict

def phi(dd):
    r=1
    for i in dd:
        r*=i**dd[i] - i**(dd[i]-1)
    return r

def factorization(n):
    dd = defaultdict(int)
    for i in range(2, int(n**0.5)+1):
        while n%i==0:
            n//=i
            dd[i]+=1
    if n>1:
        dd[n]+=1
    return dd
mod = 10**9+7
import sys
input = lambda: sys.stdin.readline().strip()

v = {}

for test in range(int(input())):
    n=int(input())
    arr=list(map(int, input().split()))
    ans = 1
    for i in arr:
        if i not in v:
            v[i] = phi(factorization(i))
        ans*=v[i]
        ans %= mod
    print(ans)