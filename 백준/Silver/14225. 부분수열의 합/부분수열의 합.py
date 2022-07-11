n=int(input())
arr = list(map(int, input().split()))
s = set()
for i in range(2**n):
    tmp = 0
    for j in range(n):
        if i&(1<<j):
            tmp+=arr[j]
    s.add(tmp)
s = list(s)
s.sort()
ans = -1
for i in range(len(s)):
    if i != s[i]:
        ans = i
        break
else:
    ans = len(s)
print(ans)