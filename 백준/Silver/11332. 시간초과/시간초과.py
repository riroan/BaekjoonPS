import sys
def input(): return sys.stdin.readline().strip()


for test in range(int(input())):
    s = input().split()
    n, t, l = map(int, s[1:])
    limit = 10**8*l
    ok = True
    if s[0] == 'O(N)':
        ok = n*t <= limit
    elif s[0] == 'O(N^2)':
        ok = n**2*t<=limit
    elif s[0] == 'O(N^3)':
        ok = n**3*t<=limit
    elif s[0] == 'O(2^N)':
        u = 1
        for i in range(n):
            u*=2
            if u*t>limit:
                ok = False
                break
    else:
        u = 1
        for i in range(1,n+1):
            u*=i
            if u*t>limit:
                ok = False
                break
    if ok:
        print("May Pass.")
    else:
        print("TLE!")
