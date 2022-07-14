n=input()
ans = 0
for i,v in enumerate(list(map(int, input().split()))):
    if i+1 != v:
        ans+=1
print(ans)