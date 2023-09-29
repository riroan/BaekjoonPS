import sys
input = lambda: sys.stdin.readline().strip()

def do(cnt, brr):
    for i in brr:
        cnt[i] -= 1
    l = 0
    for i in cnt:
        if i > 0:
            l += 1
    return l

for test in range(int(input())):
    n=int(input())
    arr=  [list(map(int, input().split()))[1:] for i in range(n)]
    ss = set()
    for i in arr:
        ss |= set(i)
    l = len(ss)
    cnt = [0]*51
    for i in arr:
        for j in i:
            cnt[j]+=1
    ans = 0
    for i in range(51):
        if cnt[i] > 0:
            s = []
            for j in arr:
                if i in j:
                    s.extend(j)
            ll = do(cnt.copy(), s)
            if ll != l:
                ans = max(ll, ans)
    print(ans)

