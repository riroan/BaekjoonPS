n,a,b = map(int, input().split())
ans = 0
for i in range(1,1000):
    if a*i >= n:
        break
    if (n-a*i)%b == 0:
        ans = 1
print(ans)
