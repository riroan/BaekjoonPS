n, k = map(int, input().split())
arr = [int(input()) for i in range(n)]
arr.sort()
l = 0
r = 2*10**9
while l+1 < r:
    mid = (l+r)//2
    cnt = 1
    v = arr[0]
    for i in range(n):
        if v + mid <= arr[i]:
            v = arr[i]
            cnt += 1
    if cnt < k:
        r = mid
    else:
        l = mid
print(l)