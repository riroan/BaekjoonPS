from itertools import permutations
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
ans = 98765432100000

for i in permutations([i for i in range(n)]):
    t = 0
    ok = True
    for j in range(n-1):
        if arr[i[j]][i[j+1]] == 0:
            ok = False
        t+=arr[i[j]][i[j+1]]
    if arr[i[-1]][i[0]] == 0:
        ok = False
    t+=arr[i[-1]][i[0]]
    if ok:
        ans = min(ans, t)
print(ans)