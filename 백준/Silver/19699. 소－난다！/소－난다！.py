from itertools import combinations
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
n,k = map(int, input().split())
arr = list(map(int, input().split()))
ss = set()
for i in combinations(arr, k):
    s = sum(i)
    if isPrime(s):
        ss.add(s)
ss = list(ss)
ss.sort()
if len(ss) == 0:
    print(-1)
else:
    print(*ss)