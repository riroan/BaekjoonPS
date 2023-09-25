import sys
input = lambda: sys.stdin.readline().strip()

ans = 0
for _ in range(int(input())):
    a,b = map(int, input().split())
    a,b= min(a,b), max(a,b)
    if b == 136:
        ans += 1000
    elif b == 142:
        ans += 5000
    elif b == 148:
        ans += 10000
    elif b == 154:
        ans += 50000
print(ans)
