import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
arr = list(input())
ans = 0
d = {i: 0 for i in "LRSK"}
for i in arr:
    if i == 'L':
        d[i] += 1
    elif i == 'R':
        if d["L"]:
            d["L"]-=1
            ans += 1
        else:
            break
    elif i == 'S':
        d[i] += 1
    elif i == 'K':
        if d["S"]:
            d["S"]-=1
            ans += 1
        else:
            break
    else:
        ans+=1
print(ans)