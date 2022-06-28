n, k, s = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
arr= arr[::-1]
ans = 0
ss = 0
for i in arr:
    ss+=i
    ans+=1
    if ss >= k*s:
        break
print(ans)