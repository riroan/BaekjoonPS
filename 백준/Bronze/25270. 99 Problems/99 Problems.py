arr = []
for i in range(100):
    arr.append(int(str(i)+'99'))
m = 987654321000
ans = 0
n = int(input())
for i in arr:
    if abs(n-i) <= m:
        m = abs(n-i)
        ans = i
print(ans)