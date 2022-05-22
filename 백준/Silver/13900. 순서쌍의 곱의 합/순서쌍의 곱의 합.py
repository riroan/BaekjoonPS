n = int(input())
arr = list(map(int, input().split()))
s = [0]
for i in arr[::-1]:
    s.append(s[-1]+i)
ans = 0
for i in range(n-1):
    ans+=arr[i] * s[-i-2]
print(ans)