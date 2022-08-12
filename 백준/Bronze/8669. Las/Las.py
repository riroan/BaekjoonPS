import sys
input = lambda: sys.stdin.readline().strip()

s = set()
for test in range(int(input())):
    a,b=map(int, input().split())
    s.add(b)
print(len(s))