import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    s = input()
    n=len(s)
    for i in range(n):
        if s[i] == 'D':
            print(i)
            break
    else:
        print(n)