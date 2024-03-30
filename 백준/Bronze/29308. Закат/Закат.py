# author:  riroan
# created:  2024.03.30 11:33:48
import sys
def input(): return sys.stdin.readline().strip()


ma = 0
s = ""
for test in range(int(input())):
    a, b, c = input().split()
    a = int(a)
    if a > ma and c == "Russia":
        ma = a
        s = b
print(s)
