from bisect import bisect_left
import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    s = input()
    n = len(s)
    k = []
    ss = []
    for i in range(n-3):
        if s[i:i+4] == 'KICK':
            k.append(i)
    for i in range(n-4):
        if s[i:i+5] == 'START':
            ss.append(i)
    ans = 0
    print(f"Case #{test+1}: ",end="")
    for i in k:
        ans += len(ss) - bisect_left(ss, i)
    print(ans)
