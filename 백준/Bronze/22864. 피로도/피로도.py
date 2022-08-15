a,b,c,m=map(int, input().split())
f = 0
ans = 0
for i in range(24):
    if f+a>m:
        f=max(f-c,0)
    else:
        f+=a
        ans+=b
print(ans)