import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    s =input()
    l = len(s)
    if s[l//2] == s[l//2-1]:
        print("Do-it")
    else:
        print("Do-it-Not")