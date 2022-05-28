n = int(input())

l, r = 0, 10**9
while l+1 < r:
    mid = (l+r)//2
    cnt = 0
    for i in range(1, 13):
        cnt+=mid//pow(5, i)
    if cnt < n:
        l=mid
    else:
        r = mid
cnt = 0
for i in range(1, 13):
    cnt += r//pow(5, i)
if cnt != n:
    print(-1)
else:
    print(r)