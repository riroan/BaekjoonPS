from collections import defaultdict
import sys
def input(): return sys.stdin.readline().strip()


for test in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    v = [0]*n
    ans = [1]*n
    for i in range(n):
        if v[i]:
            continue
        p = [i]
        d = defaultdict(int)
        current = i
        flag = 1
        while d[current] == 0:
            d[current] = len(p)
            if v[current]:
                flag = 0
                break
            v[current] = 1
            current = arr[current]-1
            p.append(current)
        for i in p[d[current]-1: -1]:
            ans[i] = 0
    print(sum(ans))