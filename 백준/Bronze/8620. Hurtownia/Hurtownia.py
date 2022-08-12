from collections import defaultdict
d =defaultdict(int)
import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    a,b=input().split()
    b= b.replace("+","")
    b=int(b)
    d[a]+=b
for i in sorted(d.keys()):
    print(i, d[i])