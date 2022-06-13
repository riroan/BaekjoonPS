import sys
input = sys.stdin.readline
n, q = map(int, input().split())
cnt = [0]*(n+1)
s = 0
m = 0
for i in range(q):
    a, b, c = map(int, input().split())
    if a == 1:
        cnt[c-1] += b
        if c-1 < n:
            s += b
            m = max(m, cnt[c-1])
    else:
        if (s+c) < (cnt[n]+b-(n>1))*n and m < cnt[n]+b:
            print("YES")
        else:
            print("NO")
