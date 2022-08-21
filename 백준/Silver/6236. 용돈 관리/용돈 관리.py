n,m = map(int, input().split())
arr = [int(input()) for i in range(n)]
l=0
r=10**18
while l+1<r:
    x=l+r>>1
    cnt = 0
    current = 0
    if max(arr) > x:
        l=x
        continue
    for i in range(n):
        if current < arr[i]:
            current = x
            cnt+=1
        current-=arr[i]
    if cnt > m:
        l = x
    else:
        r = x
print(r)