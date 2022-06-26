import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    a,b=map(int, input().split())
    ans = 0
    for i in range(a, b+1):
        ans += str(i).count('0')
    print(ans)