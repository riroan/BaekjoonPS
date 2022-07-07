import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    print(f"Case #{test+1}: ",end="")
    n,t = map(int, input().split())
    e = int(input())
    arr = [list(map(int, input().split())) for i in range(e)]
    ans = [0]*n
    dd = defaultdict(list)
    for x, y in arr:
        if x == t:
            continue
        dd[x].append(y)
    able = True
    for i in dd:
        dd[i].sort(reverse=True)
        ok = False
        l = len(dd[i])
        s = 0
        cnt = 0
        for j in dd[i]:
            s+=j
            cnt+=1
            if s >= l:
                ok = True
                break
        able &= ok
        ans[i-1] = cnt
    if not able:
        print("IMPOSSIBLE")
    else:
        print(*ans)