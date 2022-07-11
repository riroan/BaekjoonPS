n=int(input())
arr=list(map(int, input().split()))
s = int(input())
start = 0
while s and start < n:
    m = -1
    for i in range(start, min(start+s+1, n)):
        if arr[i] > m:
            m = arr[i]
            ix = i
    t = arr[ix]
    for i in range(ix-1,start-1,-1):
        arr[i+1] = arr[i]
    arr[start] = t
    s-=min(ix-start, n)
    start+=1
print(*arr)