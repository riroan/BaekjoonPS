from itertools import combinations
import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    n, k = map(int, input().split())
    print("The bit patterns are")
    ans = []
    for i in combinations([i for i in range(n)], k):
        arr = ['0']*n
        for j in i:
            arr[j] = '1'
        ans.append(''.join(arr))
    for i in ans:
        print(i)
    print()