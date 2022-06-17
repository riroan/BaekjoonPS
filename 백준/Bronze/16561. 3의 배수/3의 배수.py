n = int(input())
ans = 0
for i in range(3, n, 3):
    for j in range(3, n, 3):
        for k in range(3, n, 3):
            ans += (i+j+k) == n
print(ans)