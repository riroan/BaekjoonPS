n = 1299710
sieve = [1]*n
sieve[0] = sieve[1] = 0
for i in range(2, n):
    if sieve[i] == 0:
        continue
    for j in range(2*i,n,i):
        sieve[j] = 0
primes = []
for i, v in enumerate(sieve):
    if v:
        primes.append(i)
s = set(primes)
import sys
from bisect import bisect_left
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    k=int(input())
    if k in s:
        print(0)
        continue
    ix = bisect_left(primes, k)-1
    print(primes[ix+1]-primes[ix])