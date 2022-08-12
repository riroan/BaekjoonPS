n=int(input())
arr = list(map(int, input().split()))
ans = [0]
s = 0
for i in range(n):
    t = arr[i] * (i+1) - sum(ans)
    ans.append(t)
print(*ans[1:])