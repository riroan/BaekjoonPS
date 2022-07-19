n=int(input())
arr = list(map(int, input().split()))
m = int(input())
if sum(arr)<=m:
    print(max(arr))
else:
    l=0
    r = 10**18
    while l+1<r:
        x = (l+r)//2
        tmp = 0
        for i in arr:
            tmp += min(i, x)
        if tmp > m:
            r = x
        else:
            l = x
    print(l)