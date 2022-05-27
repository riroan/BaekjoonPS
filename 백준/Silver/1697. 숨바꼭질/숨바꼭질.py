from collections import deque
q = deque()
n, k = map(int, input().split())
v = [False] * 100001
q.append((n, 0))
v[n] = True


def check(x):
    if 0 <= x <= 100000:
        if not v[x]:
            return True
        return False
    return False


while q:
    ix, d = q.popleft()
    if ix == k:
        print(d)
        break
    if check(ix-1):
        v[ix-1] = True
        q.append((ix-1,d+1))
    if check(ix+1):
        v[ix+1] = True
        q.append((ix+1, d+1))
    if check(2*ix):
        v[ix*2] = True
        q.append((ix*2, d+1))
