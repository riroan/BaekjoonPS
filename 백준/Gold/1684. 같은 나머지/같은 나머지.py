import math
n = int(input())
arr=list(map(int, input().split()))
arr.sort()
d = []
for i in range(n-1):
    d.append(arr[i+1]-arr[i])
g = d[0]
for i in range(1, len(d)):
    g = math.gcd(g, d[i])
ans = []
for i in range(2, int(g ** 0.5)+1):
    if g % i == 0:
        ans.append(i)
        ans.append(g//i)
ans.append(g)
print(max(ans))
