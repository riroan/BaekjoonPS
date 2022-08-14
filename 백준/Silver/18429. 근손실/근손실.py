from itertools import permutations
n, k =map(int, input().split())
arr = list(map(int,input().split()))

ans = 0
for i in permutations(arr):
    ok = 1
    s = 0
    for j in i:
        s += j
        s-=k
        if s <0:
            ok = 0
            break
    ans+=ok
print(ans)