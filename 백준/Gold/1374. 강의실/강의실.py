import heapq
n = int(input())
arr = [list(map(int, input().split()))[1:] for i in range(n)]
arr.sort(key=lambda x: (x[0], x[1]))
ans = []
for i in range(n):
    if i == 0:
        heapq.heappush(ans, arr[i][1])
    else:
        if ans[0] <= arr[i][0]:
            heapq.heappop(ans)
        heapq.heappush(ans, arr[i][1])
print(len(ans))
