import sys
from itertools import permutations
def input(): return sys.stdin.readline().strip()


for test in range(int(input())):
    arr = list(map(int, input().split()))[1:]
    ans = 0
    for i in permutations(arr):
        m = 987654321
        start = 0
        for j in range(1,len(i)):
            if i[j] != i[j-1]+1:
                m = min(m, j-start)
                start = j
        m = min(m, len(i)-start)
        ans = max(ans, m)
    print(f"Case #{test+1}: {ans}")