n,m = map(int, input().split())
arr = set(map(int, input().split()))
brr = set(map(int, input().split()))
ans = 0
for i in arr:
    if i not in brr:
        ans+=1
for i in brr:
    if i not in arr:
        ans+=1
print(ans)