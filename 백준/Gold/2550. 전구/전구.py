import bisect


def lis(n, arr):
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

    u = max(ix)
    ans = []
    for i in range(n-1, -1, -1):
        if ix[i] == u:
            ans.append(arr[i])
            u -= 1
    ans.reverse()
    return ans



n = int(input())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
dd = {}
for i in range(n):
    dd[brr[i]] = i
crr = [dd[i] for i in arr]
ans = lis(n, crr)
ans = [brr[i] for i in ans]
ans.sort()

print(len(ans))
print(*ans)