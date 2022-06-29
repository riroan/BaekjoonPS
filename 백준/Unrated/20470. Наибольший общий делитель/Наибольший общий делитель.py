import math
n, d = map(int, input().split())
arr = list(map(int, input().split()))
brr = []
for i in arr:
    if i%d == 0:
        brr.append(i)
brr.sort()
ans = []
for i in range(1, len(brr)):
    if math.gcd(brr[0], brr[i]) == d:
        ans = [brr[0], brr[i]]
if ans:
    print(len(ans))
    print(*ans)
else:
    print(-1)