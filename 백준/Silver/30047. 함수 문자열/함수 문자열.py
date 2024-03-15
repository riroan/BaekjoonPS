# author:  riroan
# created:  2023.10.29 12:53:49
import sys
def input(): return sys.stdin.readline().strip()


s = input()
st = []
ok = 1
for i in s[::-1]:
    if i == 'x':
        st.append(0)
    elif i == 'g':
        if not st:
            ok = 0
            break
        st[-1] += 1
    elif i == 'f':
        if len(st) < 2:
            ok = 0
            break
        x = st.pop()
        y = st.pop()
        st.append(min(x,y))
ok &= len(st) == 1
if ok:
    print(st[0])
else:
    print(-1)
