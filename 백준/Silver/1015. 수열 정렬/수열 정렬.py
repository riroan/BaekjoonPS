
n = int(input())
arr = list(map(int, input().split()))
arr = [(v,i) for i,v in enumerate(arr)]
arr.sort(key=lambda x:x[0])
ans = [0]*n
for i,v in enumerate(arr):
    ans[v[1]] = i
print(*ans)