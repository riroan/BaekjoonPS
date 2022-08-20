n=int(input())
arr = list(map(int, input().split()))
s=[]
ans = [-1]*n
for i in range(n):
    while s:
        if s[-1][0] >= arr[i]:
            break
        x, ix = s.pop()
        ans[ix] = arr[i]
    s.append([arr[i], i])
print(*ans)