n,k = map(int, input().split())
arr = list(map(int, input().split()))
brr = [0]*n
ans = 0
while arr.count(0)<k:
    arr = [arr[-1]] + arr[:-1]
    brr = [0]+brr[:-1]
    for i in range(n-1, -1, -1):
        if i == n-1:
            brr[i] = 0
        else:
            if brr[i] and brr[i+1] == 0 and arr[i+1] > 0:
                brr[i] = 0
                brr[i+1] = 1
                arr[i+1]-=1
    if arr[0] > 0 and brr[0] == 0:
        brr[0] = 1
        arr[0]-=1
    ans+=1
print(ans)