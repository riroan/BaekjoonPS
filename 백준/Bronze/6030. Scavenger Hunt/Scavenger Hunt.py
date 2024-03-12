# author:  riroan
# created:  2024.03.12 13:35:19
import sys
input = lambda: sys.stdin.readline().strip()

p, q = map(int, input().split())
a = set()
b = set()
for i in range(1, int(p**.5)+1):
    if p%i==0:
        a.add(i)
        a.add(p//i)
for i in range(1, int(q**.5)+1):
    if q % i == 0:
        b.add(i)
        b.add(q//i)
a = sorted(list(a))
b = sorted(list(b))
for i in a:
    for j in b:
        print(i,j)
