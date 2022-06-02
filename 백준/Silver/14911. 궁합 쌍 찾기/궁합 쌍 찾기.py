arr = list(map(int, input().split()))
k = int(input())
arr.sort()
ans = set()
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == k:
            ans.add((arr[i],arr[j]))
ans = list(ans)
ans.sort(key = lambda x:(x[0],x[1]))
for i in ans:
    print(*i)
print(len(ans))