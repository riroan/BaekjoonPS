x, y = map(int, input().split())
z = 100*y//x
l, r = 0, 2*10**9
while l+1 < r:
    mid = (l+r)//2
    zz = int((y+mid)*100//(x+mid))
    if zz>z:
        r = mid
    else:
        l = mid
if z >= 99:
    print(-1)
else:
    print(r)