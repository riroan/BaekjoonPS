import sys
def input(): return sys.stdin.readline().strip()


def check(x, y):
    return 0 <= x < n and 0 <= y < n


for test in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]
    ans = 0
    for i in range(n):
        t = 0
        x, y = 0, i
        d = 0
        while True:
            if not check(x+d, y+d):
                break
            t+=arr[x+d][y+d]
            d += 1
        ans = max(t, ans)
    for i in range(n):
        t = 0
        x, y = i,0
        d = 0
        while True:
            if not check(x+d, y+d):
                break
            t+=arr[x+d][y+d]
            d += 1
        ans = max(t, ans)
    print(f"Case #{test+1}: ",end="")
    print(ans)