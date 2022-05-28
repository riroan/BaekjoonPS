import bisect

n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
arr.sort(key=lambda x:x[0])
dd = {i[1]:i[0] for i in arr}
arr = [i[1] for i in arr]
brr = [-9876543210]
ix = [0] * n

for i in range(n):
    if arr[i] > brr[-1]:
        brr.append(arr[i])
        ix[i] = len(brr) - 2
    else:
        t = bisect.bisect_left(brr, arr[i])
        brr[t] = arr[i]
        ix[i] = t-1

print(n-(len(brr) - 1))
d = {i:True for i in arr}
u = max(ix)
ans = []
for i in range(n-1, -1, -1):
    if ix[i] == u:
        ans.append(arr[i])
        u -= 1
ans.reverse()
for i in ans:
    d[i] = False
for i in [dd[i] for i in d if d[i]]:
    print(i)