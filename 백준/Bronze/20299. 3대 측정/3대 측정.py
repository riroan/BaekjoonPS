n,k,l=map(int, input().split())
ans = []
cnt = 0
for i in range(n):
    a,b,c = map(int, input().split())
    if a+b+c < k:
        continue
    if a < l or b < l or c < l:
        continue
    ans +=[a,b,c]
    cnt+=1
print(cnt)
print(*ans)