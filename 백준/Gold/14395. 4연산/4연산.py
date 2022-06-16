from collections import deque
a, b = map(int, input().split())
if a == b:
    print(0)
elif b == 1:
    print("/")
else:
    ans = 987654321
    ss = []
    q = deque()
    q.append([a*2, '+'])
    if a > 1:
        q.append([a**2, '*'])
        q.append([1, '/'])
    while q:
        n, s = q.pop()
        if len(s) > ans:
            continue
        if n > b:
            continue
        if n == b:
            if len(s) > ans:
                continue
            if len(s) < ans:
                ans = len(s)
                ss = []
                ss.append(s)
                continue
            ss.append(s)
        q.append([n*2, s+'+'])
        if n > 1:
            q.append([n**2, s+'*'])

    if len(ss) == 0:
        print(-1)
    else:
        ss.sort()
        print(ss[0])
