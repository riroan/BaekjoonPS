mod = 10**9+7
n =int(input())
p = {}
for i in range(n):
    a,b=map(int, input().split())
    if b > 0:
        p[b-1] = b*a
ans = 0
for i in p:
    ans += p[i] * pow(2, i, mod)
    ans %= mod
print(ans)
