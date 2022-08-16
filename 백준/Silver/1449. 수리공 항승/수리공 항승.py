n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
c = arr[0]-0.5
ans = 1
for i in range(n):
    if arr[i] > c+k:
        ans+=1
        c = arr[i]-0.5
print(ans)