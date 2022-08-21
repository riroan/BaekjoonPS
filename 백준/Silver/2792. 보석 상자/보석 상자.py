n,m = map(int, input().split())
arr = [int(input()) for i in range(m)]
l=0
r = 2*10**9
while l+1<r:
    x=l+r>>1
    cnt = 0
    for i in range(m):
        cnt+=arr[i]//x
        if arr[i]%x:
            cnt+=1
    if cnt > n:
        l=x
    else:
        r=x
print(r)