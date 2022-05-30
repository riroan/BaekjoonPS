import sys
input = sys.stdin.readline

def change(n, b):
    s = 0
    for ix, i in enumerate(str(n)[::-1]):
        if int(i)>=b:
            return 0
        s+=int(i) * b**ix
    return s

for test in range(int(input())):
    a, b, c = map(int, input().split())
    for i in range(2, 17):
        aa = change(a, i)
        bb = change(b, i)
        cc = change(c, i)
        if aa*bb*cc == 0:
            continue
        if aa*bb==cc:
            print(i)
            break
    else:
        print(0)