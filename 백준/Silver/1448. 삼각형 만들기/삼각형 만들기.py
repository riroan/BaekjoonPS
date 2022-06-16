n = int(input())
arr = [int(input()) for i in range(n)]
arr.sort()
ans = -1
for i in range(n-2):
    if arr[i+2] < arr[i]+arr[i+1]:
        ans = max(ans, sum(arr[i:i+3]))
print(ans)