from collections import deque
n=int(input())
for i in range(n):
    a,b = map(int, input().split())
    q = deque([[a,b,0]])
    while q:
        s,t,c = q.popleft()

        if s == t:
            print(c)
            break
        if s > t:
            continue
        q.append([s*2, t+3, c+1])
        q.append([s+1, t, c+1])