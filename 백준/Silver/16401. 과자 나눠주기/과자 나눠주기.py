m,n = map(int, input().split())
arr = list(map(int, input().split()))
l=0
r=10**18
while l+1<r:
    x=l+r>>1
    cnt = 0
    for i in range(n):
        cnt+=arr[i] // x
    if cnt >= m:
        l=x
    else:
        r=x
print(l)