from heapq import *
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
arr.sort(key=lambda x:(x[0], x[1]))
q = []
heappush(q, arr[0][1])
for s, e in arr[1:]:
    if q[0] <= s:
        heappop(q)
    heappush(q, e)
print(len(q))