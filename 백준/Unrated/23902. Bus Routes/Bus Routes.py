import sys
def input(): return sys.stdin.readline().strip()


for test in range(int(input())):
    n, d = map(int, input().split())
    arr = list(map(int,input().split()))
    l, r = 1, 10**13
    while l+1 < r:
        mid = (l+r)//2
        ok = True
        t = mid
        for i in range(n):
            t = max(t, (t+arr[i]-1)//arr[i]*arr[i])
            if t>d:
                ok = False
                break
        if ok:
            l = mid
        else:
            r = mid
    print(f"Case #{test+1}: ",end="")
    print(l)