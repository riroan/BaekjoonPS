n,s,r=map(int, input().split())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
brr.sort()
ans = 0
cnt = [0]*n
for i in arr:
    cnt[i-1] = 1
for i in range(len(brr)):
    if cnt[brr[i]-1]:
        cnt[brr[i]-1] = 0
        brr[i] = -1
for i in brr:
    if i == -1:
        continue
    if i == 1:
        cnt[1] = 0
    elif i == n:
        cnt[i-2] = 0
    else:
        if cnt[i-2]:
            cnt[i-2]=0
        else:
            cnt[i] = 0
ans1 = sum(cnt)

cnt = [0]*n
for i in arr:
    cnt[i-1] = 1
for i in brr:
    if i==-1:
        continue
    if i == 1:
        cnt[1] = 0
    elif i == n:
        cnt[i-2] = 0
    else:
        if cnt[i]:
            cnt[i] = 0
        else:
            cnt[i-2] = 0
ans2 =sum(cnt)
print(min(ans1,ans2))