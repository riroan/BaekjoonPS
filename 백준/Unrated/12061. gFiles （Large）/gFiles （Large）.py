import sys
def input(): return sys.stdin.readline().strip()


def check(n):
    for x, y in arr:
        if (y*100)//n != x:
            return False
    return True


for test in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]
    l = 0
    r = 10**18
    print(f"Case #{test+1}: ", end="")
    ok = False
    for x, y in arr:
        if x == 100:
            print(y)
            ok = True
            break
    if ok:
        continue
    while l+1 < r:
        mid = (l+r)//2
        flag = 0
        for x, y in arr:
            t = (y*100)//mid
            # print(t,x, l, r)
            if t > x:
                l = mid
                flag = 1
                break
            elif t < x:
                r = mid
                flag = 1
                break
        if flag == 0:
            break
    if mid > 1:
        ok = not(check(mid-1) | check(mid + 1)) and check(mid)
    else:
        ok = not(check(mid + 1)) and check(mid)
    
    if ok or mid > 10**15:
        print(mid)
    else:
        print(-1)
