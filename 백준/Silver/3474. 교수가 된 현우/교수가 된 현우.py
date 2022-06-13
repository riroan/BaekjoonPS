import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    n=int(input())
    t = 5
    ans = 0
    while t <= n:
        ans += n//t
        t*=5
    print(ans)