import sys
import math
from decimal import Decimal
def input(): return sys.stdin.readline().strip()


def check(n):
    for x, y in arr:
        t = (y*100)//n
        if x == 100 and n > y:
            return False
        if math.floor(t) != x:
            return False
    return True


for test in range(int(input())):
    n = int(input())
    arr = [list(map(Decimal, input().split())) for i in range(n)]
    print(f"Case #{test+1}: ", end="")
    ok = False
    for i in arr:
        if i[0] == 100:
            print(i[1])
            ok = True
            break
    if ok:
        continue
    ans = []
    for answer in range(1, 2001):
        if check(Decimal(answer)):
            ans.append(answer)
    if len(ans) == 1:
        print(ans[0])
    else:
        print(-1)
