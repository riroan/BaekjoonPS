# author:  riroan
# created:  2023.10.27 08:56:03
import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
s = set([int(input()) for i in range(n)])
a = set()
for i in range(1, max(s)+1):
    if i not in s:
        a.add(i)
if not a:
    print("good job")
else:
    a = sorted(list(a))
    for i in a:
        print(i)

