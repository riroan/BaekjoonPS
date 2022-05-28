import bisect

n = int(input())
arr = list(map(int, input().split()))

brr = [-987654321]
for i in range(n):
    if arr[i] > brr[-1]:
        brr.append(arr[i])
        continue
    t = bisect.bisect_left(brr, arr[i])
    brr[t] = arr[i]

print(n-(len(brr) - 1))