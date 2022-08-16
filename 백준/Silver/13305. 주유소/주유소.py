n=int(input())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
ans = 0
t = 0
i = 0
while i < n:
    s = 0
    for j in range(i+1, n):
        s+=arr[j-1]
        if brr[j] < brr[i]:
            ans += brr[i] * s
            i = j
            break
    else:
        ans += brr[i] * s
        break
print(ans)