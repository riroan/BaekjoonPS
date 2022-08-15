n, m = map(int, input().split())
arr = [int(input()) for i in range(int(input()))]


def check(current, x):
    return current <= x < current+m

ans = 10**18
cnt = 0
current = 0
for i in arr:
    if check(current, i):
        continue
    while i < current:
        current-=1
        cnt+=1
    while i >= current+m:
        current+=1
        cnt+=1
ans = min(ans, cnt)
print(ans-1)