n, k = map(int, input().split())
arr = list(map(int, input().split()))
l, r = 0, 4*10**9
while l+1 < r:
    mid = (l+r)//2
    t = 0
    for i in arr:
        t += max(i-mid, 0)
    if t < k:
        r=mid
    else:
        l=mid
print(l)