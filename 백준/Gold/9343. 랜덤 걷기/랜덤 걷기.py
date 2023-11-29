# author:  riroan
# created:  2023.11.29 22:06:31
import sys
def input(): return sys.stdin.readline().strip()


mod = 10**9+7
fact = [1]
inv = []
for i in range(2000005):
    fact.append(fact[-1] * (i+1))
    fact[-1] %= mod
inv.append(pow(fact[-1], mod-2, mod))
for i in range(2000005, 0, -1):
    inv.append(inv[-1]*i)
    inv[-1] %= mod
inv.reverse()

for test in range(int(input())):
    n = int(input())
    a = fact[2*n]
    b = inv[n]
    c = inv[n+1]
    print(((a*b)%mod*c)%mod)
