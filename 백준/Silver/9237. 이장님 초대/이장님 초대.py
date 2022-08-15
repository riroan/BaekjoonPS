n = int(input())
arr = list(map(int, input().split()))
arr.sort()
arr.reverse()
ans = 0
for i in range(n):
    ans = max(ans, i+arr[i])
print(ans+2)