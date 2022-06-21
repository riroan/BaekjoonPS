import sys
def input(): return sys.stdin.readline().strip()


ans = 0
for test in range(int(input())):
    a, b, c, d = map(int, input().split())
    if a == b == c == d:
        ans = max(ans, 50000+a*5000)
    elif a == b == c or a == b == d or a == c == d or b == c == d:
        if a == b == c or a == b == d or a == c == d:
            ans = max(ans, a*1000+10000)
        else:
            ans = max(ans, b*1000+10000)
    elif len(set([a, b, c, d])) == 2:
        if a == b:
            ans = max(ans, 2000+a*500+c*500)
        elif a == c:
            ans = max(ans, 2000+a*500+b*500)
        elif a == d:
            ans = max(ans, 2000+a*500+b*500)
    elif len(set([a, b, c, d])) == 3:
        if a == b:
            ans = max(ans, 1000+a*100)
        elif a == c:
            ans = max(ans, 1000+a*100)
        elif a == d:
            ans = max(ans, 1000+a*100)
        elif b == c:
            ans = max(ans, 1000+b*100)
        elif b == d:
            ans = max(ans, 1000+b*100)
        elif c == d:
            ans = max(ans, 1000+c*100)
    else:
        ans = max(ans, 100*max([a,b,c,d]))
print(ans)
