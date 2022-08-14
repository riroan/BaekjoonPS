n, h = map(int, input().split())
arr = [int(input()) for i in range(n)]
arr.sort()
ans = 10**18
t = 0
cnt =0
for i in arr[::-1]:
    t+=i
    cnt+=1
    if t >= h:
        break
print(cnt)