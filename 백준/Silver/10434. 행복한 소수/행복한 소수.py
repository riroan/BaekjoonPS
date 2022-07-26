import sys


def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def input(): return sys.stdin.readline().strip()

def f(n):
    ret = 0
    while n:
        ret+=(n%10)**2
        n//=10
    return ret
for test in range(int(input())):
    n = list(map(int, input().split()))[1]
    print(test+1, n, end=" ")
    if not isPrime(n):
        print("NO")
        continue
    s = set([n])
    while True:
        t = f(n)
        if t in s:
            break
        s.add(t)
        n=t
    if 1 in s:
        print("YES")
    else:
        print("NO")