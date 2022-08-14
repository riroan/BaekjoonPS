from itertools import combinations
import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    n=int(input())
    arr=list(map(int, input().split()))
    for i in combinations([i for i in range(n*2)], n):
        a = [arr[j] for j in i]
        b = [arr[j] for j in range(n*2) if j not in i]
        a.sort()
        b.sort()
        ok = True
        for i,j in zip(a, b):
            if j//4*3 != i:
                ok = False
        if ok:
            print(f"Case #{test+1}:",*a)
            break