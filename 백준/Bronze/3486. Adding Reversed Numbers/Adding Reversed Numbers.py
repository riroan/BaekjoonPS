# author:  riroan
# created:  2023.10.23 19:18:20
import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    a,b = input().split()
    a = int(a[::-1])
    b = int(b[::-1])
    c = str(a+b)
    print(int(c[::-1]))
