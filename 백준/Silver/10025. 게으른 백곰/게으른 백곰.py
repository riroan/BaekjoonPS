n, k = map(int, input().split())
x = [0] * 5000000
for i in range(n):
    a, b = list(map(int, input().split()))
    x[b] = a

m = 0
s = 0
for i in range(2*k+1):
    s += x[i]
m = s
l = 0
r = 2*k
while r < 1000001:
    s -= x[l]
    l += 1
    r += 1
    s += x[r]
    m = max(m, s)
print(m)
