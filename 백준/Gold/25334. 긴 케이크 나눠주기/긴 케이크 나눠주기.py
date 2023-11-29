# author:  riroan
# created:  2023.11.29 22:11:35
import sys
def input(): return sys.stdin.readline().strip()
mod = 10**9+7

def inverseEuler(n, mod):
    return pow(n, mod-2, mod)

f = [1] * (1000000+1)
for i in range(2, 1000000+1):
    f[i] = (f[i-1]*i) % mod
def C(n, r):
    return (f[n]*((inverseEuler(f[r], mod)*inverseEuler(f[n-r], mod)) % mod)) % mod


for test in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    c = s.count('1')
    if c%k:
        print(0)
        continue
    if c == 0:
        print(C(n-1, k-1))
        continue
    if k == 1:
        print(1)
        continue
    arr = []
    for i in range(n):
        if s[i] == '1':
            arr.append(i)
    t = c//k
    ans = 1
    for i in range(t, c, t):
        ans *= arr[i] - arr[i-1]
        ans %=mod
    print(ans)
