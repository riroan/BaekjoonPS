from itertools import permutations
n, k = map(int, input().split())
if n == 1:
    print(1)
else:
    arr = [i+1 for i in range(n)]
    ans = []
    for i in permutations(arr):
        a = i
        while len(a) > 1:
            brr = []
            for j in range(len(a)-1):
                brr.append(a[j]+a[j+1])
            a= brr
        if brr[0] == k:
            ans.append(i)
    ans.sort()
    print(*ans[0])