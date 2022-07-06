n = int(input())
arr = list(map(int, input().split()))
start = 0
ans = 0
for i in range(n):
    if arr[i] > arr[start]:
        ans = max(i-start-1, ans)
        start = i
ans = max(n-start-1, ans)
print(ans)