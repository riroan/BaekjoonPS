n = int(input())
arr = [int(input()) for i in range(n)]
arr.sort()
ans = 0
for i in range(n):
    ans += abs(arr[i]-i-1)
print(ans)