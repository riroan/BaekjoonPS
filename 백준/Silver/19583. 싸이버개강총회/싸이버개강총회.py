from collections import defaultdict
s,e,q=input().split()
s=list(map(int, s.split(":")))
e = list(map(int, e.split(":")))
q = list(map(int, q.split(":")))
s = s[0]*60+s[1]
e = e[0]*60+e[1]
q = q[0]*60+q[1]
arr = []
d = {}
while True:
    try:
        t,n = input().split()
        t = list(map(int, t.split(":")))
        t = t[0]*60+t[1]
        if n not in d:
            d[n] = [0,0]
        if t <= s:
            d[n][0] = 1
        if e<=t<=q:
            d[n][1] = 1
    except:
        break
ans = 0
for i in d:
    if sum(d[i]) == 2:
        ans+=1
print(ans)