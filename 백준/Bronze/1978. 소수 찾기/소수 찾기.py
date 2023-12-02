n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    f = i > 1
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            f = False
    if f:
        cnt += 1
print(cnt)
