arr = list(map(int, input().split()))
ans = 0
brr = [0]*10
def func(before=-1, ix=0,cnt=0):
    global ans
    if ix == 10:
        ok = 0
        for i, j in zip(arr,brr):
            if i == j:
                ok +=1
        ans+=ok>=5
        return
    for i in range(1, 6):
        if cnt == 2 and before == i:
            continue
        brr[ix] = i
        if before != i:
            func(i, ix+1, 1)
        else:
            func(i, ix+1, cnt+1)
func()
print(ans)