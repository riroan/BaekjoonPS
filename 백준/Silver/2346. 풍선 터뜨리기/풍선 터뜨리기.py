from collections import deque
n =int(input())
arr = list(map(int, input().split()))
arr = [(arr[i], i+1) for i in range(n)]
ans = []
q = deque(arr)
while q:
    x, ix = q.popleft()
    ans.append(ix)
    if not q:
        break
    if x>0:
        for i in range(x-1):
            q.append(q.popleft())
    if x<0:
        for i in range(-x):
            q.appendleft(q.pop())
print(*ans)