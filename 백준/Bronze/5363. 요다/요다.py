import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    s=input().split()
    print(*(s[2:]+s[:2]))