n, s = input().split()
n = int(n)
arr = [input() for i in range(n)]
l= 0
ans = ''
def check(a, b):
    if len(a) +1 != len(b):
        return False
    l,r = 0,0
    flag = False
    while l < len(a) and r < len(b):
        if flag and a[l] != b[r]:
            return False
        if not flag and a[l] != b[r]:
            flag = True
            r+=1
            if a[l]!= b[r]:
                return False
        l+=1
        r+=1
    return True

def dfs(ss):
    global ans, l
    ok = False
    if l < len(ss):
        ans = ss
        l = len(ss)
    for i in arr:
        if check(ss, i):
            ok = True
            dfs(i)

dfs(s)
print(ans)