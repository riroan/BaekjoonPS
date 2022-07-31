n=int(input())
arr = list(map(int, input().split()))
arr.sort()
k = int(input())
if k in arr:
    print(0)
else:
    if arr[0] != 1:
        arr= [0] + arr
    if arr[-1] != 1000:
        arr.append(1001)
    for i in range(len(arr)-1):
        if arr[i] < k < arr[i+1]:
            l=arr[i]+1
            r = arr[i+1]-1
            break
    ans = 0
    for i in range(l, r+1):
        for j in range(i+1, r+1):
            if i<=k<=j:
                ans+=1
    print(ans)