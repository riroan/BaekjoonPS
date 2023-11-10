from collections import Counter
n=int(input())
arr = Counter(list(map(int, input().split())))
ans = 0
for i in arr:
    ans += min(arr[i],2)
print(ans)
